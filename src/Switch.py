import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)

#Push Button to trigger Face Recognition
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Push Button to trigger Text Recognition
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

count = 0

while True:
    Button_Faces = GPIO.input(20)
    Button_Text = GPIO.input(21)
    if Button_Faces == False:
        print "Calling the function for face recognition"
        subprocess.call('python Faces.py', shell=True )
        print "Finished calling Faces.py"
    if Button_Text == False:
        print "Calling the function for reading text"
        subprocess.call('python Text.py', shell=True )
		print "Finished calling Text.py"
        
    
 


    
'''
while time_elapsed < 5 :
        if input_state == False:
            count = count+1 
            print "Count: "+str(count)
            time.delay(.1)
            input_state == True
        end_time =time.time()
        time_elapsed = end_time - start_time
    print "elapsed time: ",time_elapsed
    print "Count after 5 sec: "+str(count)#+" /n"
    count = 0


if input_state == False:
        count = count+1 
        print "button pressed"
'''
