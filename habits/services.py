from rest_framework.response import Response

from config.settings import TELEGRAM_BOT_TOKEN
import requests


def send_telegram_message(chat_id: int, text: str, *args, **kwargs):
    """
    Function sent message to "chat_id" with "text"
    """
    telegram_api_url = "https://api.telegram.org"
    telegram_bot_token = TELEGRAM_BOT_TOKEN
    method_name = 'sendmessage'
    url = f'{telegram_api_url}/bot{telegram_bot_token}/{method_name}'
    data = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url=url, data=data)
    return response.json()
