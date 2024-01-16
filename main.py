from guild_report import guild_roster_generator


guild_names = [
    "NOPE",
    "League of Shadows",
    "Flush",
    "Bad Iron",
    "nakama"

]


def init():
    for guild in guild_names:
        guild_roster_generator('us', 'chaos-bolt', guild.lower().replace(" ", "-"), 0, 25)


init()
