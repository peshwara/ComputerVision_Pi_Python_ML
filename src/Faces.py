import io
import picamera
import cv2
import numpy
from time import sleep
import subprocess

#Creating a memory stream so photos dont need to be saved in a file
stream = io.BytesIO()

#Gen the picture (low res)

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 960)#320, 240) #160, 120)
    camera.start_preview()
    sleep(8)
    camera.stop_preview()
    camera.hflip=True
    camera.capture(stream, format='jpeg')

#convert pic to numpy array
buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)

#Now create an openCV image
image = cv2.imdecode(buff, 1)

#load a cascade file for detecting faces
faces_cascade = cv2.CascadeClassifier('/home/pi/Desktop/Beginning/faces.xml')

#convert to gray
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#look for faces
faces = faces_cascade.detectMultiScale(gray, 1.1, 5)

test = "Found " +str(len(faces))+ " faces"
subprocess.call('echo '+test+'|festival  --tts', shell=True )

#Draw a rectangle around
for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)
    


#save
cv2.imwrite('result.jpg',image)
filename = "zFaces"
file = open(filename, 'w')
file.write(test)
file.close()
#subprocess.call('festival --tts '+filename, shell=True)
