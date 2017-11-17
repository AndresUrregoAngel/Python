import boto

conn = boto.connect_s3('xxx' ,'xxx')
bucket = conn.create_bucket('file')

