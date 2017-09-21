import requests
import datetime
import json

'''
def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    print("value1 = " + event['key1'])
    print("value2 = " + event['key2'])
    print("value3 = " + event['key3'])
    return event['key1']  # Echo back the first key value
    #raise Exception('Something went wrong')
'''

def lambda_handler(event, context):
    file = 'website-here'
    result = requests.get(file)
    data = result.json()
    now = datetime.datetime.now()
    hour = now.hour
    day = now.day
    month = now.month
    mins = now.minute


    with open('Bixi_%s_%s_%s-%s.json' % (month,day,hour,mins) , 'w') as outfile:
        json.dump(data, outfile)
    return print("download succeed")

lambda_handler('n','n')


