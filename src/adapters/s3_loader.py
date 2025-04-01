s3_loader.py
import boto3
import pandas as pd
from io import StringIO

class S3Loader:
    def __init__(self, bucket_name, region='us-east-1'):
        self.s3 = boto3.client('s3', region_name=region)
        self.bucket_name = bucket_name

    def load_csv(self, file_key):
        csv_obj = self.s3.get_object(Bucket=self.bucket_name, Key=file_key)
        body = csv_obj['Body'].read().decode('utf-8')
        return pd.read_csv(StringIO(body))
