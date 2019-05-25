# Import libraries
import os
import cv2
import json
import random
import numpy

def image_string(image):
    image_encode=cv2.imencode('.jpg',image)[1]
    imagelist=image_encode.tolist()
    image_string=json.dumps(imagelist)
    return image_string

def string_image(imagestring):
    image_list=json.loads(imagestring)
    arr=np.array(image_list)
    arr=np.uint8(arr)
    image=cv2.imdecode(arr,cv2.IMREAD_COLOR)
    return image


def predict(sudostring):
    filelist=[f for f in os.listdir("/container/part1") if f.endswith(".jpg")]
    index=random.randint(0,10000)
    random_image=cv2.imread("/container/part1/"+str(filelist[index]))
    while random_image is None:
        index=random.randint(0,10000)
        random_image=cv2.imread("/container/part1/"+str(filelist[index]))
    
    print("\n[INFO] Get a Input Request!")
    inputstring=image_string(random_image)
    inputstring=str(inputstring)
    return inputstring





