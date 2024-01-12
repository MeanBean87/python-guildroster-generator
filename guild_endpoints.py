import requests
from bnet_auth import create_bnet_access_token

ns_string = {
    0: "profile-classic1x-",
    1: "profile-classic-",
}

ep_type = {
    0: "",
    1: "/activity",
    2: "/achievements",
    3: "/roster",
}


async def get_guild_info(region, realm, name, namespace_id, endpoint, locale='en_US'):
    try:
        token = create_bnet_access_token()
        url = (f'https://{region}.api.blizzard.com/data/wow/guild/{realm}/{name}' +
               f'{ep_type[endpoint]}?namespace={ns_string[namespace_id]}{region}&locale={locale}&access_token={token}')

        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error in request: {e}")
        return None
