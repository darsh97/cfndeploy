import boto3
import shutil
import hashlib
import json

with open("lambda_src/products.json", "r") as config:
    config_contents = json.load(config)

def get_digest(file_path):
    h = hashlib.sha256()

    with open(file_path, 'rb') as file:
        while True:
            # Reading is buffered, so we can read smaller chunks.
            chunk = file.read(h.block_size)
            if not chunk:
                break
            h.update(chunk)

    return h.hexdigest()


s3_bucket_name = config_contents["bucket"]
zip_file_name = f"code-{get_digest('lambda_src/products.json')}"
shutil.make_archive(zip_file_name, 'zip', "lambda_src/")
s3 = boto3.resource('s3')
s3.meta.client.upload_file(f"{zip_file_name}.zip", s3_bucket_name, zip_file_name)
