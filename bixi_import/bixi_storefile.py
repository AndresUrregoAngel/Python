import boto3
from botocore.client import Config

xxxxxx = 'xxxx'
xxxx= 'xxx'
BUCKET_NAME = 'x'

s3 = boto3.resource(
    's3',
    aws_access_key_id=xxxx,
    aws_secret_access_key=xxxxxxx,
    config=Config(signature_version='s3v4')
)


for bucket in s3.buckets.all():
    print(bucket.name)

FILE_NAME = 'file'
s3_client = boto3.client('s3')
s3_client.upload_file(FILE_NAME, BUCKET_NAME, FILE_NAME)
