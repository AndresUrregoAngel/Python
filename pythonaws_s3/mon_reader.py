import boto3
import datetime
import datetime
ts = datetime.datetime.now() #.timestamp()


# Create an S3 client
s3 = boto3.client('s3')  #Client
s3resource = boto3.resource('s3') #Ressources


# Call S3 to list current buckets
response = s3.list_buckets()
# Get a list of all bucket names from the response
#for bucket in s3resource.buckets.all():
 #   print(bucket.name)

buckets = []

for bucket in response['Buckets']:
    buckets.append(bucket)

for name in buckets:
    for i in s3resource.Bucket(name).objects.all():
        print("bucket {} objects {} ".format(name,i))


# Load a file

filename = "test_"+str(ts.now())
filepath = 'C:\\Users\\a_urrego\\Documents\\DW Project\\datasources\\test.txt'
bucket_name = 'poc-developers'
s3.upload_file(filepath, bucket_name, filename)

