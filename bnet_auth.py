import requests
import os
from dotenv import load_dotenv


def create_bnet_access_token():
    load_dotenv()

    client_id = os.getenv('BNET_ID')
    client_secret = os.getenv('BNET_SECRET')

    data = {'grant_type': 'client_credentials'}
    response = requests.post('https://%s.battle.net/oauth/token' % "us", data=data, auth=(client_id, client_secret))
    return response.json()['access_token']
