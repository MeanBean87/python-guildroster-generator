import asyncio
from guild_endpoints import get_guild_info
from character_endpoints import get_character_info, get_parse_data
from pandas_functions import generate_guild_roster_report
from role import RUNE_ROLE_MAP, WOW_CLASSES

testing = False


# Gets specified guilds player roster
async def get_guild_roster(region, realm, name, namespace_id, min_level):
    report = await get_guild_info(region, realm, name, namespace_id, 3)
    roster = {member['character']['name']: {"level": member['character']['level']}
              for member in report.get("members", []) if member['character']['level'] >= min_level}
    return roster


# Updates class and average item level for members
async def get_character_specializations(region, realm, roster, namespace_id):
    iteration = 1
    print("Adding class and average item level to members")
    for member in roster:
        profile_summary = get_character_info(region, realm, member.lower(), namespace_id, 0)
        try:
            roster[member]["average_item_level"] = profile_summary["average_item_level"]
            roster[member]["class"] = profile_summary["character_class"]["name"]
            print(f'{iteration} of {len(roster)} members updated')
        except KeyError:
            roster[member]["average_item_level"] = "Unknown Item Level"
            roster[member]["class"] = "Unknown Class"
            print(f'Failed to get class and item level for {member}')
        iteration += 1
    return roster


# Updates character runes for members
async def get_character_runes(region, realm, roster, namespace_id):
    iteration = 1
    print("Adding currently equipped runes to members")
    for member in roster:
        try:
            equipment_summary = get_character_info(region,
                                                   realm, member.lower(), namespace_id, 1)['equipped_items']
            found_runes = 1
            if 'runes' not in roster[member]:
                roster[member]['runes'] = []
            for item in equipment_summary:
                for enchantment in item.get('enchantments', []):
                    if enchantment.get('enchantment_slot', {}).get('type') == 'TEMPORARY':
                        roster[member]['runes'].append(enchantment['display_string'])
                        found_runes += 1
            print(f'{iteration} of {len(roster)} members updated')
        except KeyError:
            roster[member]["runes"] = []
            print(f'Failed to get equipped runes for {member}')
        iteration += 1
    return roster


# Determines role based from runes
async def get_character_roles(roster):
    iteration = 1
    print("Adding members roles")
    for member in roster:
        try:
            scores = {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0}
            for rune in roster[member]['runes']:
                role_scores = RUNE_ROLE_MAP.get(rune, {})
                for role in role_scores:
                    scores[role] += role_scores[role]
            calculated_role = max(scores, key=scores.get)
            roster[member]["role"] = calculated_role
            print(f'{iteration} of {len(roster)} members updated')
        except KeyError:
            roster[member]["role"] = "Unknown"
            print(f'Failed to get class and item level for {member}')
        iteration += 1
    return roster


# Updates talent point spread
async def get_character_talents(region, realm, roster, namespace_id):
    iteration = 1
    print("Adding members talent point spreads")
    for member in roster:
        talent_tree = {spec_name: 0 for spec_name in WOW_CLASSES.get(roster[member]['class'], {})}
        specialization_summary = get_character_info(region, realm, member.lower(), namespace_id, 8)
        try:
            for specialization in specialization_summary.get('specialization_groups', []):
                for spec in specialization.get('specializations', []):
                    spec_name = spec.get('specialization_name', '')
                    spent_points = spec.get('spent_points', 0)
                    talent_tree[spec_name] += spent_points
            roster[member]['talent_points'] = talent_tree
            print(f'{iteration} of {len(roster)} members updated')
        except KeyError:
            roster[member]["talent_points"] = "Unknown"
            print(f'Failed to get talent points for {member}')
        iteration += 1
    return roster


async def get_character_parse(roster, realm, region):
    iteration = 1
    print("Adding Blackfathom Deeps DPS Parses")
    for member in roster:
        best_performance_average = get_parse_data(member.lower(), realm, region)
        roster[member]["bfd_parse"] = round(best_performance_average['zoneRankings']['bestPerformanceAverage'], 1)
        print(f'{iteration} of {len(roster)} members updated')
        iteration += 1
    return roster


# Wrapper function for generating the report
async def generate_guild_report(region, realm, guild_name, namespace_id, min_level):
    roster = await get_guild_roster(region, realm, guild_name, namespace_id, min_level)
    if testing:
        roster = {'Voov': {'level': 25},
                  'Krix': {'level': 25}}
    roster = await get_character_specializations(region, realm, roster, namespace_id)
    roster = await get_character_runes(region, realm, roster, namespace_id)
    roster = await get_character_roles(roster)
    roster = await get_character_talents(region, realm, roster, namespace_id)
    roster = await get_character_parse(roster, realm, region)
    generate_guild_roster_report(roster, guild_name)


# Async Report Init
def guild_roster_generator(region, realm, guild_name, namespace_id, min_level):
    asyncio.run(generate_guild_report(region, realm, guild_name, namespace_id, min_level))
