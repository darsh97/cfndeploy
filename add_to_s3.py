import boto3
import shutil
import hashlib
import json

with open("lambda_src/products.json", "r") as config:
    config_contents = json.load(config)


# S3CodeKey=code-8d296273ad81efc8f3397a67d1a958438b83f9da3b630fcb50e11254b91ac470.zip


def get_digest(file_path):
    with open(file_path, "r") as f:
        for line in f.readlines():
            m = hashlib.sha256(line.encode('utf8'))
        return m.hexdigest()


s3_bucket_name = config_contents["bucket"]
zip_file_name = f"code-{get_digest('lambda_src/products.json')}"
shutil.make_archive(zip_file_name, 'zip', "lambda_src/")
s3 = boto3.resource('s3')
s3.meta.client.upload_file(f"{zip_file_name}.zip", s3_bucket_name, zip_file_name)
