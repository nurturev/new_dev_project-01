import boto3

# Replace with your desired bucket name and region
bucket_name = "nv-dataset-models"
region = "ap-south-1"

s3 = boto3.client('s3')

try:
    response = s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={'LocationConstraint': region}
    )
    print(f"Bucket '{bucket_name}' created successfully.")
except Exception as e:
    print(f"Error creating bucket: {e}")
