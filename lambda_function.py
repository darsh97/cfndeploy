import json
import products


def lambda_handle(event, context):
    with open('products.json', r) as f:
        content = json.load(f)
        for product in content['products']:
            print(product)