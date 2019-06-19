# -*- coding: utf-8 -*-

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import os

#load the classifiers downloaded 
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

cap = cv.VideoCapture(0)
path = "G:\Forsk_MLDL\Day 27"# path were u want store the data set
id = input('Enter user name')

try:
    
    os.mkdir(path+str(id))
    print("Directory " , path+str(id),  " Created ") 
except FileExistsError:
    print("Directory " , path+str(id) ,  " already exists")
sampleN=0;

while 1:

    ret, img = cap.read()
    frame = img.copy()


    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    for (x,y,w,h) in faces:
        sampleN = sampleN+1
        cv.imwrite(path+str(id)+ "\\" +str(sampleN)+ ".jpg", gray[y:y+h, x:x+w])
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        roi_color = img[y:y+h, x:x+w]
        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        cv.waitKey(100)
    cv.imshow('img',img)

    cv.waitKey(1)

    if sampleN > 40:

        break

cap.release()

cv.destroyAllWindows()


