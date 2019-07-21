import os  
import glob  
import time
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

LEDPin1 = 17
i =0
GPIO.setup(LEDPin1, GPIO.OUT)

os.system('modprobe w1-gpio')  
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'  
device_folder = glob.glob(base_dir + '28*')[0]  
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    
    f = open(device_file, 'r')  
    lines = f.readlines()  
    f.close()  
    return lines

def read_temp():  
    lines = read_temp_raw()
    
    while lines[0].strip()[-3:] != 'YES':  
        time.sleep(0.2)  
        lines = read_temp_raw()  
    equals_pos = lines[1].find('t=')  
    if equals_pos != -1:  
        temp_string = lines[1][equals_pos+2:]

        #Converting the string t to float
        #And dividing the 5 digit value by 1000
        C = float(temp_string) / 1000.0  
        F = C * 9.0 / 5.0 + 32.0  
        return F

while True:  
    temperature = read_temp()
    print(temperature)
    if temperature > 80.0:
        GPIO.output(LEDPin1, True)
        
    if temperature < 80.0:
        GPIO.output(LEDPin1, False)
