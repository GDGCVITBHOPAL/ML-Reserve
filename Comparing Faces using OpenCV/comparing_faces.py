from face_recognition.api import face_distance
import numpy as np
import cv2
import face_recognition 

'''Loading images'''
img =face_recognition.load_image_file('Comparing Faces using OpenCV\Images\steve.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# face_recoginition works with rgb 
imgTest = face_recognition.load_image_file('Comparing Faces using OpenCV\Images\stevetest.jpg')
#imgTest = face_recognition.load_image_file('Comparing Faces using OpenCV\Images\elon_test.jpg')
imgTest= cv2.resize(imgTest , (300,300))
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

'''Finding face'''
faceLocation= face_recognition.face_locations(img)[0]
encodeimg = face_recognition.face_encodings(img)[0]
cv2.rectangle(img,(faceLocation[3],faceLocation[0]),(faceLocation[1],faceLocation[2]), (255,0,255),2)


faceLocationTest= face_recognition.face_locations(imgTest)[0]
encodeimgTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocationTest[3],faceLocationTest[0]),(faceLocationTest[1],faceLocationTest[2]), (255,0,255),2)

'''Testing with another image'''

results = face_recognition.compare_faces([encodeimg], encodeimgTest)

faceDistance= face_recognition.face_distance([encodeimg],encodeimgTest)

cv2.putText(imgTest , f'{results} {round(faceDistance[0],2)}',(20,50), cv2.FONT_HERSHEY_COMPLEX ,1,(0,0,255),2)

print(results,faceDistance)

cv2.imshow('img',img)
cv2.imshow('imgTest',imgTest)
cv2.waitKey(0)
cv2.destroyAllWindows()
