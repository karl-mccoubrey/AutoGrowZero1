from RPi.GPIO import GPIO

GPIO_MODE = GPIO.BOARD
PINOUT = {
    'TEMP': 7,
    'TEMP_HUMIDITY': None,
    'LIGHT_RELAY': None,
    'HEATER_RELAY': None,
    'VENT_RELAY': None
}