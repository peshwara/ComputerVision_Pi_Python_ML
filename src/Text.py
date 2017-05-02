import io
import picamera
import cv2
import numpy
from time import sleep
from PIL import Image
from pytesser import *
import subprocess

#Creating a memory stream so photos dont need to be saved in a file
stream = io.BytesIO()

#Ger the picture (low res)

with picamera.PiCamera() as camera:
    camera.resolution = (640,480)
    camera.start_preview()
    sleep(7)
    camera.stop_preview()
    camera.capture(stream, format='jpeg')
print "capturing the image.."

#convert pic to numpy array
buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)

#Now create an openCV image
image = cv2.imdecode(buff, 1)


#convert to gray
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
(T, bin) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)


#convert to gray
#gray_inv = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
(T, bin_inv) = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY_INV)



#save
cv2.imwrite('result.tif', gray)
cv2.imwrite('result_inv.tif', bin_inv)


words = call_tesseract('result.tif', 'outtext')
words1 = call_tesseract('result_inv.tif', 'outtext_inv')


filename = "outtext.txt"
file = open(filename)
test=file.read()
file.close()


filename2 = "outtext_inv.txt"
file2 = open(filename2)
test=file2.read()
file2.close()


subprocess.call('festival --tts '+filename, shell=True)
subprocess.call('festival --tts '+filename2, shell=True)

#subprocess.call('echo '+words+'|festival  --tts', shell=True )
