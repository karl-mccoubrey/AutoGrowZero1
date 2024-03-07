
def log_data_to_firebase(item):
    match item['action']:
        case 'getTemp':
            # log temp
            log_temperature_to_firebase(item['data'])
        case _:
            # default
            print('default case hit for logDataToFirebase. Please check data and try again.')
            
            
            
def log_temperature_to_firebase(data):
    print('logging temp to fb')