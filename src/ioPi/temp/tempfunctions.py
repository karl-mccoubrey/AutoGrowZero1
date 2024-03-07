import RPi.GPIO as GPIO
from ...config.pinout import PINOUT
from ...config.config import IS_DEV

def get_temperature():
    if IS_DEV:
        return PINOUT['TEMP']
    else:
        return GPIO.input(PINOUT['TEMP'])