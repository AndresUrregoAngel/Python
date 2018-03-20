import boto3
import datetime

# Create an S3 client
s3 = boto3.client('s3')  #Client
s3resource = boto3.resource('s3') #Ressources

"""
# Call S3 to list current buckets
response = s3.list_buckets()
# Get a list of all bucket names from the response
for bucket in s3resource.buckets.all():
    print(bucket.name)

for bucket in response['Buckets']:
    print(bucket['Name'])

"""
# Load a file

filename = '',
filepath = 'C:\\Users\\a_urrego\\Documents\\DW Project\\datasources\\test.txt'
bucket_name = 'poc-developers'
s3.upload_file(filename, bucket_name, filepath)
