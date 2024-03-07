from flask import Flask
from .apifunctions import handle_log_temperature
from ..ioPi.temp.tempfunctions import get_temperature
app = Flask(__name__)

@app.route("/hello-world")
def hello_world():
    print('hello world')
    return "<p>Hello, World!</p>"

@app.route("/temperature/get_temperature")
def get_temp():
    print('get_temperature')
    temperature = get_temperature()
    print('Temperature: {t}'.format(t = temperature))
    return "<p>{t} C</p>".format(t = temperature)
@app.route("/temperature/log_temperature")
def log_temp():
    print('log_temperature')
    handle_log_temperature()
    
