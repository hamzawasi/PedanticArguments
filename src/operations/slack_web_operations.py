import logging
logging.basicConfig(level=logging.ERROR)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackWebOperations:
    def __init__(self, webClient):
        pass