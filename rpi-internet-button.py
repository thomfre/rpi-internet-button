import RPi.GPIO as GPIO
import os

internet_on = False

def enable_internet():
	global internet_on
	if internet_on == False:
		print("Enabling internet")
		os.system("ifup eth1")
		internet_on = True

def disable_internet():
	global internet_on
	if internet_on == True:
		print("Disabling internet")
		os.system("ifconfig eth1 down")
		internet_on = False

def button_callback(channel):
	if GPIO.input(channel) == GPIO.HIGH:
		enable_internet()
	else:
		disable_internet()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(7, GPIO.BOTH, callback = button_callback)

while True:
	GPIO.input(7)
	#Do nothing


GPIO.cleanup()
