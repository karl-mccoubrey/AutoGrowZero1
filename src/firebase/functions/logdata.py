
def log_data_to_firebase(item):
    # match statement var
    matchItem = item['action']
    
    # match statement to determine action to handle 
    #match matchItem:
    #    case 'getTemp':
    #        # log temp
    #        log_temperature_to_firebase(item['data'])
    #    case _:
    #        # default
    #        print('default case hit for logDataToFirebase. Please check data and try again.')
    
    
    if matchItem == 'getTemp':
        # log temperature
        log_temperature_to_firebase(item['data'])
    elif matchItem == 'PLACEHOLDER': 
        # DO SOMETHING
        print('placeholder elif')
    else:
        #default
        print('default case hit for logDataToFirebase. Please check data and try again.')
    
            
            
            
def log_temperature_to_firebase(data):
    print('logging temp to fb')