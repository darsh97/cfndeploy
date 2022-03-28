import json
from typing import final
import requests

CONFIG_FILE: final = "./config.json"
ACCESS_TOKEN: final = "access_token"


def get_config_file_details(config_file_path: str):
    with open(config_file_path, "r") as f:
        config = json.load(f)
    return config


def lambda_handler(event, context):
    config = get_config_file_details(CONFIG_FILE)
    access_token = config[ACCESS_TOKEN]

    headers = {
        "Authorization": f"token {access_token}",
        "Accept": "application/vnd.github.v3+json",
    }
