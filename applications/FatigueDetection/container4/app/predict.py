import cv2
import numpy as np
import os
import json
import time
from timeit import default_timer as timer
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

load_start=timer()

protoFile = "/container/pose_deploy_linevec.prototxt"
weightsFile = "/container/pose_iter_440000.caffemodel"
net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)
nPoints = 18
POSE_PAIRS = [ [1,0],[1,2],[1,5],[2,3],[3,4],[5,6],[6,7],[1,8],[8,9],[9,10],[1,11],[11,12],[12,13],[0,14],[0,15],[14,16],[15,17]]

# input image dimensions for the network
inWidth = 368
inHeight = 368

COUNT=0

load_end=timer()

print("\n[INFO] C4 LOAD:"+str(load_end-load_start))

def predict(imagestring):
    start=timer()
    if imagestring is None:
        end=timer()
        print("\n[INFO] c4 time: "+str(end-start))
        print("\n[INFO] Pose Detection FINISHED!")
        return False
    frame=string_image(imagestring)
    frameCopy = np.copy(frame)
    frameWidth = frame.shape[1]
    frameHeight = frame.shape[0]
    threshold = 0.1
   
    inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight),
                              (0, 0, 0), swapRB=False, crop=False)
    
    net.setInput(inpBlob)
    
    output = net.forward()
    
    H = output.shape[2]
    W = output.shape[3]
    
    # Empty list to store the detected keypoints
    points = []
    add=0
    square=0
    count=0
    for i in range(nPoints):
        # confidence map of corresponding body's part.
        probMap = output[0, i, :, :]
    
        # Find global maxima of the probMap.
        minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
        
        # Scale the point to fit on the original image
        x = (frameWidth * point[0]) / W
        y = (frameHeight * point[1]) / H
    
        if prob > threshold : 
            cv2.circle(frameCopy, (int(x), int(y)), 8, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
            cv2.putText(frameCopy, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, lineType=cv2.LINE_AA)
    
            # Add the point to the list if the probability is greater than the threshold
            points.append((int(x), int(y)))
            add+=int(x)
            square+=int(x)*int(x)
            count+=1
        else :
            points.append(None)
    
    add=add/count
    variance=(square-add*add)/(count-1)
    
    # Draw Skeleton
    for pair in POSE_PAIRS:
        partA = pair[0]
        partB = pair[1]
    
        if points[partA] and points[partB]:
            cv2.line(frame, points[partA], points[partB], (0, 255, 255), 2)
            cv2.circle(frame, points[partA], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
            
    print("\n[INFO] Pose Detection FINISHED!")
    if variance>20000:
        COUNT=COUNT+1
        print("\n[INFO] WARNING! MAY BE TIRED!")
    else:
        COUNT=COUNT-1
    end=timer()
    print("\n[INFO] C4 time:"+str(end-start))
    if COUNT > 6:
        return "True"
    else:
        return "False"
    



        
        
