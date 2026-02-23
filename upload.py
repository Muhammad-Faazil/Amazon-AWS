import boto3
import os

# Create S3 resource
s3 = boto3.resource(
    's3',
    aws_access_key_id="AKIAQQJXJL6DQHNKQDG3",
    aws_secret_access_key="B384TimGXMq6W/NlIiRVx/6r736BWrpqQX/z/EJu",
    region_name="ap-south-1"
)

# Bucket name
bucket_name = "de-sixth-sem-lab-2026"

# File path on your laptop
local_file = r"C:\Users\faazi\Downloads\4SF23CI092.png"

# File name in S3
s3_file_name = "submissions/4SF23CI092.png"

# Upload file
s3.Bucket(bucket_name).upload_file(local_file, s3_file_name)

print("File uploaded successfully!")