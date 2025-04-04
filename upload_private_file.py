import boto3
from botocore.exceptions import NoCredentialsError, ClientError

# Config
bucket_name = 'my-devops-bucket-123456'
file_path = 'sample.txt'
s3_key = 'logs/sample.txt'  # Destination path in the bucket

# Create S3 client
s3 = boto3.client('s3')

try:
    s3.upload_file(
        Filename=file_path,
        Bucket=bucket_name,
        Key=s3_key,
        ExtraArgs={'ACL': 'private'}  # 👈 Ensure the file is private
    )
    print(f"✅ File '{file_path}' uploaded as private to s3://{bucket_name}/{s3_key}")
except FileNotFoundError:
    print("❌ File not found:", file_path)
except NoCredentialsError:
    print("❌ AWS credentials not found.")
except ClientError as e:
    print("❌ Client error:", e)
