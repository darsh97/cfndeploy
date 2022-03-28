import json
import time
import boto3
import os
import logging
import cfnresponse
from botocore.exceptions import ClientError

s3_client = boto3.client('s3')

with open('products.json', 'r') as config_file:
    data = json.load(config_file)
    PRODUCT_NAMES = data["products"]


def lambda_handler(event, context):
    try:
        if event['RequestType'] == 'Create':
            handle_create(event, context)
        elif event['RequestType'] == 'Update':
            handle_update(event, context)
        elif event['RequestType'] == 'Delete':
            handle_delete(event, context)
    except ClientError as exception:
        logging.error(exception)
        cfnresponse.send(event, context, cfnresponse.FAILED,
                         {}, error=str(exception))


def handle_create(event, context):
    create_folders(PRODUCT_NAMES)
    cfnresponse.send(event, context, cfnresponse.SUCCESS,
                     {})


def handle_delete(event, context):
    cfnresponse.send(event, context, cfnresponse.SUCCESS,
                     {})


def handle_update(event, context):
    cfnresponse.send(event, context, cfnresponse.SUCCESS,
                     {})


def create_folders(product_names):
    DUMMY_FILE = '/tmp/dummy.txt'

    s3_bucket = os.environ['AWS1_LAMBDA_FUNCTION_NAME']

    with open(DUMMY_FILE, 'w'):
        pass

    for product_name in PRODUCT_NAMES:
        print(f"creating folder {product_name}")
        s3_client.upload_file(DUMMY_FILE, s3_bucket, f"{product_name}/")

    return {"Status": "Completed"}