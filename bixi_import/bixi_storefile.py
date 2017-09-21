import boto3
import requests
import json
import os
from glob import glob
import datetime
from botocore.client import Config

def lambda_handler(event, context):
    x = 'x'
    x = 'x'
    BUCKET_NAME = 'x'

    s3 = boto3.resource(
        's3',
        aws_access_key_id=x,
        aws_secret_access_key=x,
        config=Config(signature_version='s3v4')
    )

    file = 'website-here'
    result = requests.get(file)
    data = result.json()
    now = datetime.datetime.now()
    hour = now.hour
    day = now.day
    month = now.month
    mins = now.minute

    a=glob("/tmp/*.json")
    for file in a:
        os.remove(file)

    with open('/tmp/Bixi_%s_%s_%s-%s.json' % (month, day, hour, mins), 'w') as outfile:
        json.dump(data, outfile)

    filename = 'Bixi_%s_%s_%s-%s.json' % (month, day, hour, mins)
    datafile = open('/tmp/Bixi_%s_%s_%s-%s.json' % (month, day, hour, mins),'rb')

    s3.Bucket(BUCKET_NAME).put_object(Key=filename, Body=datafile)
    return print("process completed succesfully")

#lambda_handler('n', 'n')
