import json
from typing import final
import requests

CONFIG_FILE: final = "./config.json"
ACCESS_TOKEN: final = "access_token"
OWNER: final = "owner"
REPO: final = "repository"
API: final = "api"
TRIGGER_REQUEST: final = "trigger"


def get_config_file_details(config_file_path: str):
    with open(config_file_path, "r") as f:
        config = json.load(f)
    return config


def lambda_handler(event, context):
    config = get_config_file_details(CONFIG_FILE)
    access_token = config[ACCESS_TOKEN]
    owner = config[OWNER]
    repo = config[REPO]
    trigger_req_api = config[API][TRIGGER_REQUEST]

    headers = {
        "Authorization": f"token {access_token}",
        "Accept": "application/vnd.github.v3+json",
    }

    trigger_requst: str = trigger_req_api.format(owner=owner, repo=repo)
