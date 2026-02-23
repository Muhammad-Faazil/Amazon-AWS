import boto3
import os
s3= boto3.resource(
    's3',
    aws_access_key_id="AKIAQQJXJL6DQHNKQDG3",
    aws_secret_access_key="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",
    region_name="ap-south-1", 
    )

my_bucket = s3.Bucket("de-sixth-sem-lab-2026")

working_dir = r"D:/AWS_skillLab/downloaded_files/"

for file in my_bucket.objects.filter(Prefix="csv/"):
    if file.key.endswith(".txt"):
        local_file_name = os.path.basename(file.key)

        print(f"Downloading {file.key} to {local_file_name}")
        my_bucket.download_file(file.key, local_file_name)
        print(f"Finishing Downloading {file.key} to {local_file_name}\n")