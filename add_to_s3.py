import boto3
import shutil

import json

with open("lambda_src/products.json", "r") as config:
    config_contents = json.load(config)

s3_bucket_name = config_contents["bucket"]
shutil.make_archive("code", 'zip', "lambda_src/")
s3 = boto3.resource('s3')
s3.meta.client.upload_file("code.zip", s3_bucket_name, "code.zip")
