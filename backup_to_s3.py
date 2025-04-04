# backup_to_s3.py
import os
import boto3
from botocore.exceptions import NoCredentialsError
from datetime import datetime

# Configuration
LOCAL_FOLDER = '/path/to/local/folder'  # Change this
BUCKET_NAME = 'your-s3-bucket-name'
S3_FOLDER = 'backups'  # e.g. store backups under "backups/"

# Create S3 client
s3 = boto3.client('s3')

def upload_files():
    for root, dirs, files in os.walk(LOCAL_FOLDER):
        for file in files:
            local_path = os.path.join(root, file)
            relative_path = os.path.relpath(local_path, LOCAL_FOLDER)
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            s3_key = f"{S3_FOLDER}/{timestamp}/{relative_path}"
            try:
                s3.upload_file(local_path, BUCKET_NAME, s3_key)
                print(f"Uploaded: {local_path} → s3://{BUCKET_NAME}/{s3_key}")
            except NoCredentialsError:
                print("AWS credentials not found. Please configure them properly.")

if __name__ == "__main__":
    upload_files()

