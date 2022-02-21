import json

import boto3

from botocore.exceptions import ClientError

from django.conf import settings
from django.core.management.base import BaseCommand


def get_read_only_s3_policy(bucket):
    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "",
                "Effect": "Allow",
                "Principal": {"AWS": "*"},
                "Action": "s3:GetBucketLocation",
                "Resource": f"arn:aws:s3:::{bucket}"
            },
            {
                "Sid": "",
                "Effect": "Allow",
                "Principal": {"AWS": "*"},
                "Action": "s3:ListBucket",
                "Resource": f"arn:aws:s3:::{bucket}"
            },
            {
                "Sid": "",
                "Effect": "Allow",
                "Principal": {"AWS": "*"},
                "Action": "s3:GetObject",
                "Resource": f"arn:aws:s3:::{bucket}/*"
            },
        ]
    }
    return policy


class Command(BaseCommand):
    def handle(self, *args, **options):
        aws_access_key_id = settings.AWS_ACCESS_KEY_ID
        aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY
        aws_endpoint_url = settings.AWS_S3_ENDPOINT_URL
        bucket = settings.AWS_STORAGE_BUCKET_NAME

        client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            endpoint_url=aws_endpoint_url,
        )

        print(f'Create bucket "{bucket}"', end=': ')
        try:
            client.create_bucket(Bucket=bucket)
            print('success')
        except ClientError as err:
            error_message = err.response['Error']
            code = error_message.get('Code')
            if code == 'BucketAlreadyOwnedByYou':
                print('already exists')
            else:
                raise

        print('Set policy', end=': ')
        policy = get_read_only_s3_policy(bucket)
        client.put_bucket_policy(Bucket=bucket, Policy=json.dumps(policy))
        print('success')
