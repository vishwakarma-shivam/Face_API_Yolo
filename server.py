from urllib.request import urlopen
import cv2
import numpy as np
from fastapi import FastAPI, Request
import uvicorn
import os
from helper import img64_to_cvImg, getImgfromURL
from utils import get_outputs_names, post_process, CONF_THRESHOLD, NMS_THRESHOLD


#Configure the model
net = cv2.dnn.readNetFromDarknet('./cfg/yolov3-face.cfg', './model-weights/yolov3-wider_16000.weights')
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


def count_faces(img):
    blob=cv2.dnn.blobFromImage(img, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    outs=net.forward(get_outputs_names(net))
    faces=post_process(img, outs, CONF_THRESHOLD, NMS_THRESHOLD)
    return len(faces)






# Create an API 
app=FastAPI()


@app.post('/api/countFace/')
async def countFace(info: Request):
    data = await info.json()
    img = img64_to_cvImg(data['img'])
    #img=img64_to_cvImg(img64)
    return {"id": data['ref'], "faceCount": count_faces(img)}

@app.post('/api/getCountByUrl/')
async def getCountByUrl(info:Request):
    data = await info.json()
    img=getImgfromURL(data['url'])
    return {"id": data['ref'], "faceCount": count_faces(img)}


if __name__=='__main__':

    ## uncomment to run locally
    #uvicorn.run(app)

    ## uncomment to run on heroku
    uvicorn.run("server:app", host='0.0.0.0', port=(int)(os.environ.get('PORT', 5000)))

    

    