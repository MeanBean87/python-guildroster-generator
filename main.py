from guild_report import guild_roster_generator


guild_names = [
    "CLAM LORDS",
    "Manabound",
    "Parts for Kravel",
    "Unfathomable"
]


def init():
    for guild in guild_names:
        guild_roster_generator('us', 'chaos-bolt', guild.lower().replace(" ", "-"), 0, 40)


init()
