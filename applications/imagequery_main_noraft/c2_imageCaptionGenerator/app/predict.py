from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from timeit import default_timer as timer
load_start = timer()

import math
import os
import json
import tensorflow as tf

print("pwd for c2/predict.py: " + os.getcwd())

import c2_imageCaptionGenerator.configuration as configuration
import c2_imageCaptionGenerator.inference_wrapper as inference_wrapper
import c2_imageCaptionGenerator.caption_generator as caption_generator
import c2_imageCaptionGenerator.vocabulary as vocabulary


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files or name in dirs:
            return os.path.join(root, name)

checkpoint_path = "/container/c2_imageCaptionGenerator/im2txt/model/newmodel.ckpt-2000000"
vocabulary_path = "/container/c2_imageCaptionGenerator/im2txt/data/word_counts.txt"

tf.logging.set_verbosity(tf.logging.INFO)

# Build the inference graph.
g = tf.Graph()
with g.as_default():
    model = inference_wrapper.InferenceWrapper()
    restore_fn = model.build_graph_from_config(
        configuration.ModelConfig(), checkpoint_path)
g.finalize()

# Create the vocabulary.
vocab = vocabulary.Vocabulary(vocabulary_path)

###### Specify GPU allocation to avoid CUDA_ERROR_OUT_OF_MEMORY #####
# Reference1: https://blog.csdn.net/wangkun1340378/article/details/72782593
config = tf.ConfigProto(allow_soft_placement=True)

# 最多占gpu资源的30%
gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.3)

#开始不会给tensorflow全部gpu资源 而是按需增加
config.gpu_options.allow_growth = True
sess = tf.Session(config=config, graph=g)

# Reference2: https://github.com/tensorflow/tensorflow/issues/14475
# gpu_fraction = 0.1
# gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=gpu_fraction)
# sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))

#######################################################################

# # create session (Original)
# sess = tf.Session(graph=g)

# Load the model from checkpoint.
restore_fn(sess)

# Prepare the caption generator.
generator = caption_generator.CaptionGenerator(model, vocab)

load_end = timer()
print("Finish preloading modules in " + str(load_end - load_start) + " seconds!")
   


def predict(image_file_index):
    start = timer()

    image_file_index = int(image_file_index)
    if image_file_index > 1000:
        return "Invalid image file index! Only index between 1 to 1000 is allowed!"

    image_file_path = "/container/c2_imageCaptionGenerator/im2txt/data/imageDataset/101_ObjectCategories/" + str(image_file_index) + ".jpg"

    captionList = ["", "", ""]
    with tf.gfile.GFile(image_file_path, "rb") as f:
        image = f.read()
        captions = generator.beam_search(sess, image)
        for i, caption in enumerate(captions):
            # Ignore begin and end words.
            sentence = [vocab.id_to_word(w) for w in caption.sentence[1:-1]]
            sentence = " ".join(sentence)
            captionList[i] = sentence
            print("  %d) %s (p=%f)" % (i, sentence, math.exp(caption.logprob)))
            # the end of caption generation

    # generated_caption = ' '.join(captionList)
    # return only the one with the highest probability
    generated_caption = captionList[0]

    end = timer()
    time_elapsed = end - start
    print("  The image file takes " + str(time_elapsed) + " seconds")

    return generated_caption, time_elapsed


if __name__ == "__main__":
    print(predict(1))
    print(predict(2))
    print(predict(3))
    print(predict(4))

