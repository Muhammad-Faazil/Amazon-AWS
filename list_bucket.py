import boto3

s3= boto3.resource(
    's3',
    aws_access_key_id="AKIAQQJXJL6DQHNKQDG3",
    aws_secret_access_key="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",
    region_name="ap-south-1", 
    )

for bucket in s3.buckets.all():
   # print(bucket.name)
    my_bucket = s3.Bucket(bucket.name)
    
    
    for file in my_bucket.objects.all():
        print(f"Bucket Name: {bucket.name} Key: {file.key}")
