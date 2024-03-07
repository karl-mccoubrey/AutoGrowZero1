from ..ioPi.temp.tempfunctions import get_temperature
from ..firebase.functions.logdata import log_data_to_firebase

def handle_log_temperature():
    temp = get_temperature()
    result = {}
    if temp:
        result = {
            'action': 'getTemp',
            'status': True,
            'data': temp,
        }
    else:
        result = {
            'action': 'getTemp',
            'status': False,
            'data': None,
        }
        
    log_data_to_firebase()
    
    return result

