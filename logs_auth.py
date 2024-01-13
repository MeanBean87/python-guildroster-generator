import requests
import os
from dotenv import load_dotenv


def create_logs_access_token():
    load_dotenv()

    client_id = os.getenv('LOGS_ID')
    client_secret = os.getenv('LOGS_SECRET')

    data = {'grant_type': 'client_credentials'}
    url = 'https://www.warcraftlogs.com/oauth/token'
    auth = (client_id, client_secret)

    response = requests.post(url, data=data, auth=auth)
    return response.json()['access_token']
