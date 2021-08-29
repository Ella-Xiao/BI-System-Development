import boto3

"""
Credentials:
https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html

Boto3-S3:
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.list_buckets
"""


class S3Client:
    def __init__(self, access_key, secret_key):
        self.access_key = access_key
        self.secret_key = secret_key
        # self.bucket_name = bucket_name
        # , bucket_name = None
        self.client = boto3.client(
            's3',
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key
        )

    def list_bucket(self):
        response = self.client.list_buckets()
        print(response)

    def download_file(self, bucket, key, target_file_path):
        response = self.client.download_file(bucket, key, target_file_path)
        print(response)

    def upload_file(self, local_file_name, bucket, s3_key):
        response = self.client.upload_file(local_file_name, bucket, s3_key)
        print(response)

