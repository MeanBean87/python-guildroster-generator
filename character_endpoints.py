import requests
from bnet_auth import create_bnet_access_token
from logs_auth import create_logs_access_token

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

query = '''
query($name: String, $serverSlug: String, $serverRegion: String, $role: RoleType!, $zoneID: Int) {
    characterData {
        character(name: $name, serverSlug: $serverSlug, serverRegion: $serverRegion) {
            name 
            zoneRankings(role: $role, zoneID: $zoneID)
        }
    }
}
'''


def get_character_info(region, realm, name, namespace_id, endpoint, locale='en_US'):
    token = create_bnet_access_token()
    url = (f'https://{region}.api.blizzard.com/profile/wow/character/{realm}/{name}' +
           f'{ep_type[endpoint]}?namespace={ns_string[namespace_id]}{region}&locale={locale}&access_token={token}')
    response = requests.get(url)
    return response.json()


def get_parse_data(name, realm, region):
    token = create_logs_access_token()
    url = 'https://vanilla.warcraftlogs.com/api/v2/client'

    variables = {
        'name': name,
        'serverSlug': realm,
        'serverRegion': region,
        'role': 'DPS',
        'zoneID': 2007
    }

    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return

    result = response.json()

    if 'errors' in result:
        print("GraphQL Errors:")
        for error in result['errors']:
            print(error['message'])
        return

    character_data = result['data']['characterData']['character']

    if character_data is None:
        print("No character data found.")
    else:
        print(character_data)

    return character_data
