import boto

conn = boto.connect_s3('AKIAIXSY423F3SSKO3IA' ,'ecfIp0cUfHeuey0lyB0YfGOJTYkQFK1+zr4Navhw')
bucket = conn.create_bucket('file')

