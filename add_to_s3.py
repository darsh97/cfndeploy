import boto3
from zipfile import ZipFile
import json

with open("products.json", "r") as config:
    config_contents = json.load(config)

s3_bucket_name = config_contents["bucket"]

FILES = (
    'lambda_function.py',
    'products.json'
)

with ZipFile("code.zip", "w") as zip_file:
    for f in FILES:
        zip_file.write(f)

s3 = boto3.resource('s3')
s3.meta.client.upload_file("code.zip", s3_bucket_name, "code.zip")
