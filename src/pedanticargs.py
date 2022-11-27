import os
import logging
from models.models import getDBinstance, init_db
from repository.pedanter_repository import PedanterRepository
logging.basicConfig(level=logging.ERROR)
from pathlib import Path
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

slack_token = os.environ["SLACK_TOKEN"]
channel_id = os.environ["CHANNEL_ID"]

init_db()

client = WebClient(token = slack_token)

try:
    response = client.chat_postMessage(
        channel = channel_id,
        text = "Hello from your app! :tada:" 
    )

    pedanter = PedanterRepository()
    pedanter.createPedanter(username='hamza', slackId= '')
except SlackApiError as exc:
    logging.exception(exc)
    assert exc.response["error"]