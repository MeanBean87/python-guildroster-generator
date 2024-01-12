CLASS_ID_NAME_MAP = {
    1: 'Warrior',
    3: 'Hunter',
    4: 'Rogue',
    5: 'Priest',
    7: 'Shaman',
    8: 'Mage',
    9: 'Warlock',
    11: 'Druid',
}

WOW_CLASSES = {
    'Warrior': {'Arms': 0, 'Fury': 0, 'Protection': 0},
    'Paladin': {'Holy': 0, 'Protection': 0, 'Retribution': 0},
    'Hunter': {'Beast Mastery': 0, 'Marksmanship': 0, 'Survival': 0},
    'Rogue': {'Assassination': 0, 'Combat': 0, 'Subtlety': 0},
    'Priest': {'Discipline': 0, 'Holy': 0, 'Shadow': 0},
    'Death Knight': {'Blood': 0, 'Frost': 0, 'Unholy': 0},
    'Shaman': {'Elemental': 0, 'Enhancement': 0, 'Restoration': 0},
    'Mage': {'Arcane': 0, 'Fire': 0, 'Frost': 0},
    'Warlock': {'Affliction': 0, 'Demonology': 0, 'Destruction': 0},
    'Monk': {'Brewmaster': 0, 'Mistweaver': 0, 'Windwalker': 0},
    'Druid': {'Balance': 0, 'Feral Combat': 0, 'Restoration': 0},
    'Demon Hunter': {'Havoc': 0, 'Vengeance': 0}
}

RUNE_ROLE_MAP = {
    # Warrior Runes
    'Flagellation': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 1, 'Tank': 0},
    'Blood Frenzy': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 1, 'Tank': 0},
    'Raging Blow': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 1, 'Tank': 0},
    'Warbringer': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 1, 'Tank': 1},

    'Furious Thunder': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 3},
    'Consumed By Rage': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 1, 'Tank': 0},
    'Frenzied Assault': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 1, 'Tank': 0},
    'Victory Rush': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 1, 'Tank': 0},

    'Endless Rage': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 1, 'Tank': 0},
    'Devastate': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 3},
    'Single-Minded Fury': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 1, 'Tank': 0},
    'Quick Strike': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 1, 'Tank': 0},

    # Warlock Runes
    'Lake of Fire': {'Healer': 0, 'Ranged DPS': 1, 'Melee DPS': 0, 'Tank': 1},
    'Master Channeler': {'Healer': 0, 'Ranged DPS': 1, 'Melee DPS': 0, 'Tank': 1},
    'Soul Siphon': {'Healer': 0, 'Ranged DPS': 1, 'Melee DPS': 0, 'Tank': 0},
    'Demonic Tactics': {'Healer': 0, 'Ranged DPS': 1, 'Melee DPS': 0, 'Tank': 0},

    'Everlasting Affliction': {'Healer': 0, 'Ranged DPS': 1, 'Melee DPS': 0, 'Tank': 1},
    'Incinerate': {'Healer': 0, 'Ranged DPS': 1, 'Melee DPS': 0, 'Tank': 1},
    'Demonic Grace': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 3},
    'Demonic Pact': {'Healer': 0, 'Ranged DPS': 1, 'Melee DPS': 0, 'Tank': 0},

    'Metamorphosis': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 3},
    'Shadow Bolt Volley': {'Healer': 0, 'Ranged DPS': 1, 'Melee DPS': 0, 'Tank': 0},
    'Chaos Bolt': {'Healer': 0, 'Ranged DPS': 1, 'Melee DPS': 0, 'Tank': 0},
    'Haunt': {'Healer': 0, 'Ranged DPS': 1, 'Melee DPS': 0, 'Tank': 0},

    # Shaman Runes
    'Dual Wield Specialization': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 3, 'Tank': 0},
    'Shield Mastery': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 3},
    'Overload': {'Healer': 1, 'Ranged DPS': 1, 'Melee DPS': 0, 'Tank': 0},
    'Healing Rain': {'Healer': 3, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},

    'Ancestral Guidance': {'Healer': 3, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},
    'Earth Shield': {'Healer': 3, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},
    'Way of Earth': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 3},
    'Shamanistic Rage': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},

    'Lava Burst': {'Healer': 0, 'Ranged DPS': 3, 'Melee DPS': 0, 'Tank': 0},
    'Lava Lash': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 3, 'Tank': 0},
    'Molten Blast': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},
    'Water Shield': {'Healer': 1, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 1},

    # Rogue Runes
    'Deadly Brew': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 1, 'Tank': 0},
    'Just a Flesh Wound': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 3},
    'Quick Draw': {'Healer': 0, 'Ranged DPS': 1, 'Melee DPS': 1, 'Tank': 0},
    'Slaughter from the Shadows': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 1, 'Tank': 0},

    'Between the Eyes': {'Healer': 0, 'Ranged DPS': 1, 'Melee DPS': 1, 'Tank': 0},
    'Blade Dance': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 3},
    'Envenom': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 1, 'Tank': 0},

    'Mutilate': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 1, 'Tank': 0},
    'Shadowstrike': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 1, 'Tank': 0},
    'Saber Slash': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 1, 'Tank': 0},
    'Shiv': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 1, 'Tank': 0},
    'Main Gauche': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 3},

    # Priest Runes
    'Void Plague': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},
    'Serendipity': {'Healer': 3, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},
    'Strength of Soul': {'Healer': 3, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},
    'Twisted Faith': {'Healer': 0, 'Ranged DPS': 3, 'Melee DPS': 0, 'Tank': 0},

    'Power Word: Barrier': {'Healer': 3, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},
    'Shared Pain': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},
    'Homunculi': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},
    'Prayer of Mending': {'Healer': 3, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},

    'Penance': {'Healer': 3, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},
    'Mind Sear': {'Healer': 0, 'Ranged DPS': 3, 'Melee DPS': 0, 'Tank': 0},
    'Circle of Healing': {'Healer': 3, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},
    'Shadow Word: Death': {'Healer': 0, 'Ranged DPS': 3, 'Melee DPS': 0, 'Tank': 0},

    # Paladin Runes
    'Seal of Martyrdom': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},
    'Divine Storm': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 1, 'Tank': 1},
    'Horn of Lordaeron': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},
    'Aegis': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 3},

    'Divine Sacrifice': {'Healer': 3, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},
    'Inspiration Exemplar': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},
    'Avengers Shield': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},
    'Exorcist': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},
    'Rebuke': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},

    'Beacon of Light': {'Healer': 3, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},
    'Crusader Strike': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},
    'Hand of Reckoning': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 3},

    # Mage Runes
    'Burnout': {'Healer': 0, 'Ranged DPS': 3, 'Melee DPS': 0, 'Tank': 0},
    'Fingers of Frost': {'Healer': 0, 'Ranged DPS': 3, 'Melee DPS': 0, 'Tank': 0},
    'Regeneration': {'Healer': 3, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},
    'Enlightenment': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},

    'Icy Veins': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},
    'Arcane Surge': {'Healer': 1, 'Ranged DPS': 1, 'Melee DPS': 0, 'Tank': 0},
    'Mass Regeneration': {'Healer': 3, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},
    'Living Flame': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},

    'Rewind Time': {'Healer': 3, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},
    'Living Bomb': {'Healer': 1, 'Ranged DPS': 1, 'Melee DPS': 0, 'Tank': 0},
    'Arcane Blast': {'Healer': 1, 'Ranged DPS': 1, 'Melee DPS': 0, 'Tank': 0},
    'Ice Lance': {'Healer': 0, 'Ranged DPS': 3, 'Melee DPS': 0, 'Tank': 0},

    # Hunter Runes
    'Heart of the Lion': {'Healer': 0, 'Ranged DPS': 1, 'Melee DPS': 1, 'Tank': 0},
    'Master Marksman': {'Healer': 0, 'Ranged DPS': 3, 'Melee DPS': 0, 'Tank': 0},
    'Lone Wolf': {'Healer': 0, 'Ranged DPS': 1, 'Melee DPS': 1, 'Tank': 0},
    'Cobra Strikes': {'Healer': 0, 'Ranged DPS': 3, 'Melee DPS': 0, 'Tank': 0},

    'Kill Command': {'Healer': 0, 'Ranged DPS': 3, 'Melee DPS': 0, 'Tank': 0},
    'Sniper Training': {'Healer': 0, 'Ranged DPS': 3, 'Melee DPS': 0, 'Tank': 0},
    'Serpent Spread': {'Healer': 0, 'Ranged DPS': 3, 'Melee DPS': 0, 'Tank': 0},
    'Flanking Strike': {'Healer': 0, 'Ranged DPS': 1, 'Melee DPS': 1, 'Tank': 0},

    'Beast Mastery': {'Healer': 0, 'Ranged DPS': 1, 'Melee DPS': 1, 'Tank': 0},
    'Chimera Shot': {'Healer': 0, 'Ranged DPS': 3, 'Melee DPS': 0, 'Tank': 0},
    'Explosive Shot': {'Healer': 0, 'Ranged DPS': 3, 'Melee DPS': 0, 'Tank': 0},
    'Carve': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 3, 'Tank': 0},

    # Druid Runes
    'Living Seed': {'Healer': 3, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},
    'Wild Strikes': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 1, 'Tank': 1},
    'Fury of Stormrage': {'Healer': 1, 'Ranged DPS': 1, 'Melee DPS': 0, 'Tank': 0},
    'Survival of the Fittest': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 3},

    'Starsurge': {'Healer': 1, 'Ranged DPS': 1, 'Melee DPS': 0, 'Tank': 0},
    'Lifebloom': {'Healer': 3, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},
    'Skull Bash': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 1, 'Tank': 1},
    'Savage Roar': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 3, 'Tank': 0},

    'Sunfire': {'Healer': 0, 'Ranged DPS': 3, 'Melee DPS': 0, 'Tank': 0},
    'Lacerate': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 3},
    'Wild Growth': {'Healer': 3, 'Ranged DPS': 0, 'Melee DPS': 0, 'Tank': 0},
    'Mangle': {'Healer': 0, 'Ranged DPS': 0, 'Melee DPS': 3, 'Tank': 0},
}
