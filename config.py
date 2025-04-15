import os

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION", "ap-south-1")
S3_BUCKET_NAME = os.getenv("AWS_S3_BUCKET_NAME", "default_bucket_name")
S3_FILE_KEY = os.getenv("AWS_S3_FILE_KEY", "default_file_key")

'''
$env:AWS_S3_BUCKET_NAME = "nv-dataset-models"
$env:AWS_S3_FILE_KEY = "dataset_tenant.csv"
'''
