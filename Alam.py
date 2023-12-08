import RPi.GPIO as GPIO
import schedule
import subprocess
import time

channel = 17 # GPIO 

# GPIO setup
GPIO.setmode(GPIO.BCM)

def job():
    GPIO.setup(channel, GPIO.OUT)
    print ("Vibration Start")
    time.sleep(30) # time in millisecond
    GPIO.cleanup()
    print ("Vibration Stop")


schedule.every().day.at("21:14").do(job) # Customize alarm time

while True:
    schedule.run_pending()
    time.sleep(1)
