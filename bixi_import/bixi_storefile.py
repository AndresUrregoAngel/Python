import boto3
from botocore.client import Config

ACCESS_KEY_ID = 'AKIAIEHQZ52XONC4JQXA'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'biximontreal'

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version='s3v4')
)


for bucket in s3.buckets.all():
    print(bucket.name)

FILE_NAME = 'Bixi_9_16_14-38.json'
s3_client = boto3.client('s3')
s3_client.upload_file(FILE_NAME, BUCKET_NAME, FILE_NAME)
