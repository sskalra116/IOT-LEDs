import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)


count = 2
LEDPin1 = 17
LEDPin2 = 22
i =0
buttonPin = 5
buttonPin2 = 6

GPIO.setup(LEDPin1, GPIO.OUT)
GPIO.setup(LEDPin2, GPIO.OUT)
GPIO.setup(buttonPin,GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(buttonPin2,GPIO.IN, pull_up_down = GPIO.PUD_UP)
pwm = GPIO.PWM(LEDPin2,100)
pwm.start(0)

buttonPress = True
buttonPress2 = True

def step2():

    count = 2
    i =0
    try:
        while True:
            GPIO.output(LEDPin1, True)
    
            buttonPress = GPIO.input(buttonPin)
            buttonPress2 = GPIO.input(buttonPin2)
            if buttonPress == False:
                sleep(2)
                nofrequency()
            if buttonPress2 == False:
                sleep(2)
                GPIO.output(LEDPin1, False)
                step22()
            print("LED ON")
            sleep(1.0/count)
            GPIO.output(LEDPin1,False)
            
            print("LED OFF")
            sleep(1.0/count)

            i+=1;
            if i%5 == 0:
                count+=1
            if count == 8:
                count = 2

            print(count)

    finally:
        GPIO.cleanup()

def nofrequency():
    count = 2
    i =0
    
    while True:
        GPIO.output(LEDPin1, True)
    
        buttonPress = GPIO.input(buttonPin)
        buttonPress2 = GPIO.input(buttonPin2)
        if buttonPress == False:
            sleep(2)
            step2()
        if buttonPress2 == False:
            sleep(2)
            GPIO.output(LEDPin1, False)
            step22()
                
        print("LED ON")
        sleep(1.0/count)
        GPIO.output(LEDPin1,False)
        
        print("LED OFF")
        sleep(1.0/count)


def step22():

    brightness = 10
    i = 1
    try:
        while True:
            
            GPIO.output(LEDPin2, True)
            buttonPress = GPIO.input(buttonPin)
            buttonPress2 = GPIO.input(buttonPin2)
            if buttonPress == False:
                sleep(1)
                pwm.ChangeDutyCycle(brightness)
                brightness+= 20
                i+=1;
            if buttonPress2 == False:
                sleep(2)
                GPIO.output(LEDPin2, False)
                step2()
            print ("brightness -" ,brightness)
        
            GPIO.output(LEDPin2,False)
            sleep(1)

            
            if i%5 == 0:
                brightness = 10

    finally:
        GPIO.cleanup()

step2()        
