import boto3

# instance an AWS CLI thru the API.
# At this point require use IAM credentials to reach our the services
client = boto3.client('firehose')  # Service name


# Method to send data in streaming to the AWS Listener
response = client.put_record(
    DeliveryStreamName='developmentpoc', # Name of the kinesis firehose
    Record={
        'Data': "this a third test for kinesis"  # data to be sent
    }
)