import base64
import numpy as np
import cv2
from urllib.request import urlopen

def img64_to_cvImg(img64):
    img64=img64.replace('data:image/jpeg;base64,','')
    img=base64.b64decode(img64)
    img=np.fromstring(img,np.uint8)
    img=cv2.imdecode(img,cv2.IMREAD_COLOR)
    return img

def getImgfromURL(url):
    req= urlopen(url)
    arr=np.asarray(bytearray(req.read()),dtype=np.uint8)
    img=cv2.imdecode(arr,-1)
    return img