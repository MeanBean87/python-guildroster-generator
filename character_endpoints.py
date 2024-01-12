import requests
from bnet_auth import create_bnet_access_token

ns_string = {
    0: "profile-classic1x-",
    1: "profile-classic-",
}

ep_type = {
    0: "",
    1: "/equipment",
    2: "/character-media",
    3: "/status",
    4: "/pvp-summary",
    5: "/statistics",
    6: "/achievements",
    7: "/achievements/statistics",
    8: "/specializations",
}


def get_character_info(region, realm, name, namespace_id, endpoint, locale='en_US'):
    token = create_bnet_access_token()
    url = (f'https://{region}.api.blizzard.com/profile/wow/character/{realm}/{name}' +
           f'{ep_type[endpoint]}?namespace={ns_string[namespace_id]}{region}&locale={locale}&access_token={token}')
    response = requests.get(url)
    return response.json()


