import boto3
from botocore.exceptions import NoCredentialsError

# Initialize the S3 client
s3_client = boto3.client('s3')

def generate_presigned_url(bucket_name, object_key, expiration=3600):
    try:
        response = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': object_key},
            ExpiresIn=expiration
        )
        return response
    except NoCredentialsError:
        return "Credentials not available."

# Example usage
bucket = 'my-private-bucket'
key = 'documents/my-private-file.pdf'

signed_url = generate_presigned_url(bucket, key)

print("Generated Signed URL:")
print(signed_url)

