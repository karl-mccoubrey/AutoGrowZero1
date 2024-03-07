from src.api.flask import app
import RPi.GPIO as GPIO
#from .src.config.pinout import GPIO_MODE, PINOUT
from src.config.pinout import PINOUT
from src.config.pinout import GPIO_MODE


GPIO.setMode(GPIO_MODE)
GPIO.setup(PINOUT['TEMP'], GPIO.IN)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=666, threaded=True)