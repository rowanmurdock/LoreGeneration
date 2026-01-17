CHARACTER_TRAITS = {
    "ambitious": {
        "power": +5,
        "stress": +2,
        "prestige": +1
    },
    "cruel": {
        "morality": +5,
        "prestige": -1
    },
    "charismatic": {
        "prestige": +5,
        "wealth": +1
    },
    "pious": {
        "morality": -3,
        "prestige": +2
    },
    "brave": {
        "morality": -3,
        "prestige": +3
    },
    "weak_willed": {
        "power": -2,
        "stress": +1
    },
    "kind": {
        "prestige": +2,
        "morality": -3,
        "power": -1
    },
    "ruthless": {
        "power": +2,
        "stress": +1,
        "morality": +2
    },
    "greedy": {
        "wealth": +3,
        "morality": +2,
        "stress": +1
    },
    "frugal": {
        "wealth": +1,
        "stress": -1
    },
    "generous": {
        "wealth": -2,
        "prestige": +2,
        "morality": -1
    },
    "corrupt": {
        "wealth": +2,
        "prestige": -2,
        "morality": +3
    },
    "stoic": {
        "stress": -3,
        "prestige": +1
    },
    "calculating": {
        "power": +1,
        "stress": -1
    },
}

CULTURE_TRAITS = {
    "Warrior Culture": {
        "war_pressure": +10,
        "stability": -2
    },
    "Pacifist": {
        "war_pressure": -8,
        "stability": +3
    },
    "Egalitarian": {
        "stability": +2,
        "religious_tension": -3
    },
    "Expansionist": {
        "war_pressure": +6,
        "resources": -2,
        "religious_tension": +1
    },
    "Isolationist": {
        "war_pressure": -3,
        "resources": +1,
        "stability": +2,
        "population": -500
    },
    "Mercantile": {
        "resources": +6,
        "stability": +1
    },
    "Agrarian": {
        "resources": +4,
        "stability": +2
    },
    "Nomadic": {
        "resources": -3,
        "war_pressure": +2,
        "stability": -3
    },
    "Urbanized": {
        "resources": +3,
        "religious_tension": +2
    },
    "Zealous": {
        "religious_tension": -5,
        "stability": -3
    },
    "Honorable": {
        "war_pressure": +2,
        "stability": +1
    },
    "Massive Feasts": {
        "stability": +3,
        "resources": -4
    },
    "Ancestor Worship": {
        "religious_tension": -4,
        "stability": +2
    },
    "Seafaring": {
        "resources": +2
    },
    "Storm Worshippers": {
        "religious_tension": -1,
        "war_pressure": +1
    },
    "Communal Labor": {
        "stability": +2,
        "resources": +2
    },
    "Debate Tradition": {
        "stability": +1,
        "religious_tension": +3
    },
    "Funeral Rites": {
        "stability": +2,
        "religious_tension": -2,
        "resources": -1
    },
    "Artistic Mentorship": {
        "stability": +4,
        "war_pressure": -2
    },
    "Massive Families": {
        "resources": -3,
        "stability": +2,
        "population": +1000
    },
    "Arena Combat": {
        "war_pressure": +5,
        "stability": -1
    },
    "Heroic Leaders": {
        "stability": +3,
        "war_pressure": +3
    },
    "Public Games": {
        "stability": +2,
        "resources": -2
    },
    "Religious Pilgrimages": {
        "religious_tension": -3,
        "stability": +2
    },
    "Caste System": {
        "stability": -5,
        "religious_tension": +3
    },
    "Public Executions": {
        "stability": -2,
        "religious_tension": +1
    },
    "Raiding Society": {
        "war_pressure": +8,
        "stability": -4,
        "resources": +2
    },
}

RELIGIOUS_TRADITIONS = {
    "Ancestor Veneration": {
        "stability": +3,
        "religious_tension": +1
    },
    "Ritual Fasting": {
        "resources": -2,
        "stability": +2
    },
    "Sacred Pilgrimage": {
        "resources": -3,
        "religious_tension": +2,
        "stability": +1
    },
    "Blood Sacrifice": {
        "religious_tension": +5,
        "war_pressure": +2
    },
    "Seasonal Offerings": {
        "resources": -2,
        "stability": +2
    },
    "Holy Silence": {
        "religious_tension": -2,
        "stability": +1
    },
    "Chanted Liturgy": {
        "stability": +2
    },
    "Sacred Fire Keeping": {
        "stability": +2,
        "resources": -1
    },
    "Trial By Ordeal": {
        "stability": -3,
        "religious_tension": +3
    },
    "Divine Kingship": {
        "stability": +4,
        "religious_tension": +3
    },
    "Scriptural Literalism": {
        "religious_tension": +4,
        "stability": +1
    },
    "Mystic Visions": {
        "stability": -2,
        "religious_tension": +2
    },
    "Communal Confession": {
        "stability": +3,
        "religious_tension": -1
    },
    "Ritual Purification": {
        "religious_tension": +2,
        "stability": +1
    },
    "Ceremonial Burial": {
        "stability": +2,
        "resources": -1
    },
    "Sun Worship": {
        "war_pressure": +1,
        "stability": +2
    },
    "Moon Vigils": {
        "religious_tension": -1,
        "stability": +1
    },
    "Sacred Music": {
        "stability": +2
    },
    "Temple Tithes": {
        "resources": +3,
        "stability": -1
    },
    "Warrior Initiation Rites": {
        "war_pressure": +4,
        "stability": -1
    },
    "Oath Binding Ceremonies": {
        "stability": +3,
        "religious_tension": +1
    },
    "Sacred Hospitality": {
        "stability": +2,
        "resources": -1
    },
    "Votive Offerings": {
        "resources": -2,
        "stability": +1
    },
    "Ascetic Withdrawal": {
        "resources": -3,
        "religious_tension": -2
    },
    "Sacred Geometry": {
        "stability": +1
    },
    "Funerary Processions": {
        "stability": +2,
        "resources": -1
    },
    "Ritual Scarification": {
        "war_pressure": +2,
        "stability": -1
    },
    "Sacred Storytelling": {
        "stability": +2
    },
    "Dream Interpretation": {
        "religious_tension": +2,
        "stability": -1
    },
    "Martyr Veneration": {
        "war_pressure": +3,
        "religious_tension": +3
    },
    "Holy Relics": {
        "stability": +2,
        "religious_tension": +2
    },
    "Divine Law Courts": {
        "stability": +3,
        "religious_tension": +2
    },
    "Purity Taboos": {
        "religious_tension": +4,
        "stability": -2
    },
    "Sacred Marriage Rites": {
        "stability": +2
    },
    "Sacramental Feasts": {
        "stability": +3,
        "resources": -2
    },
    "Prophetic Ecstasy": {
        "religious_tension": +4,
        "stability": -2
    },
    "Ancestral Masks": {
        "stability": +1,
        "religious_tension": +1
    },
    "Temple Processions": {
        "stability": +2,
        "resources": -1
    },
    "Silent Contemplation": {
        "religious_tension": -2,
        "stability": +1
    },
    "Sacred Calendars": {
        "stability": +1
    },
    "Blood Oaths": {
        "war_pressure": +3,
        "stability": -1
    },
    "Holy Warfare Doctrine": {
        "war_pressure": +6,
        "religious_tension": +3
    },
    "Ritualized Almsgiving": {
        "resources": -2,
        "stability": +2
    },
    "Cleansing Fires": {
        "religious_tension": +4,
        "stability": -3
    },
    "Forbidden Knowledge Rites": {
        "religious_tension": +5,
        "stability": -3
    },
    "Sacred Mountains": {
        "stability": +2
    },
    "Temple Slavery": {
        "resources": +3,
        "stability": -4,
        "religious_tension": +2
    },
    "Divine Judgment Rituals": {
        "religious_tension": +3,
        "stability": -2
    },
    "Sacred Waters": {
        "stability": +2
    },
    "Spirit Possession Rites": {
        "religious_tension": +3,
        "stability": -2
    },
    "Holy Fasting Seasons": {
        "resources": -2,
        "stability": +1
    },
    "Canonical Recitation": {
        "stability": +2,
        "religious_tension": +1
    },
    "Sacred Animal Totems": {
        "stability": +1,
        "religious_tension": +1
    },
    "Ritual Anointing": {
        "stability": +3
    },
    "Consecrated Battle Standards": {
        "war_pressure": +3,
        "stability": +1
    },
    "Ritual Cursing": {
        "religious_tension": +4,
        "stability": -2
    },
    "Sacred Bloodlines": {
        "stability": +3,
        "religious_tension": +2
    },
    "Divine Punishment Doctrine": {
        "religious_tension": +5,
        "stability": -3
    },
}

