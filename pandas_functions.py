import os
import pandas as pd
import subprocess

dirname = os.path.dirname(__file__)


def generate_guild_roster_report(dictionary, guild_name):
    df1 = pd.DataFrame(dictionary).T.reset_index().rename(columns={'index': 'Name'})
    df1.columns = ['Player Name', 'Level', 'Average Item Level', 'Class', 'Runes', 'Role', 'Talent Points', 'Best AVG Parse (BFD)']

    df1 = df1.style.map(color_class, subset=['Class'])
    df1 = df1.map(color_role, subset=['Role'])

    pd.set_option('display.max_colwidth', None)

    path = os.path.join(dirname, r'reports', f'{guild_name}_roster.xlsx')
    print(f'Generated a report at {path}')

    # Writing to Excel
    with pd.ExcelWriter(path, engine='xlsxwriter') as writer:
        df1.to_excel(writer, sheet_name='roster', index=False)

    subprocess.run(['start', path], shell=True)

def convert_talent_points(x):
    try:
        return ', '.join(f"{key}: {value}" for key, value in x.items())
    except (AttributeError, TypeError):
        return str(x)


def convert_runes(x):
    try:
        return ', '.join(str(each) for each in x)
    except (TypeError, ValueError):
        return str(x)


def color_class(val):
    class_colors = {
        'Warrior': 'background-color: #C79C6E',  # Warrior color: Tan
        'Paladin': 'background-color: #F58CBA',  # Paladin color: Pink
        'Hunter': 'background-color: #ABD473',  # Hunter color: Green
        'Rogue': 'background-color: #FFF569',  # Rogue color: Yellow
        'Priest': 'background-color: #FFFFFF',  # Priest color: White
        'Death Knight': 'background-color: #C41F3B',  # Death Knight color: Red
        'Shaman': 'background-color: #0070DE',  # Shaman color: Blue
        'Mage': 'background-color: #69CCF0',  # Mage color: Sky Blue
        'Warlock': 'background-color: #9482C9',  # Warlock color: Purple
        'Monk': 'background-color: #00FF96',  # Monk color: Light Green
        'Druid': 'background-color: #FF7D0A',  # Druid color: Orange
        'Demon Hunter': 'background-color: #A330C9',  # Demon Hunter color: Dark Purple
    }
    return class_colors.get(val, '')


def color_role(val):
    role_colors = {
        'Healer': 'background-color: #00FF00',  # Healer color: Green
        'Ranged DPS': 'background-color: #FFA500',  # Ranged DPS color: Orange
        'Melee DPS': 'background-color: #FF474C',  # Melee DPS color: Red
        'Tank': 'background-color: #67B7D1'  # Tank color: Blue
    }
    return role_colors.get(val, '')
