import random
from character import Character
from names import *
from faction import Faction
from culture import Culture
from religion import Religion
from event import *
from traits import *


class World:
    def __init__(self, name, year, factions, major_events):
        self.name = name
        self.year = year
        self.factions = factions
        self.major_events = major_events
        self.history = []

    def getYear(self):
        return self.year
    
    def factionEnds(self, faction):
        faction.factionEnds()
        self.major_events.append(Event(f"The faction of {faction.name} has ended in the world of {self.name}.", "Faction End", self.year, self.year))
        self.factions.remove(faction)

    
    def addHistoricalEvent(self, desc):
        self.history.append(desc)

    def generateRandomWorld(self):
        name = random.choice(WORLD_NAMES)
        year = 100
        culture_pool = [Culture.generateRandomCulture() for _ in range(random.randint(5, 10))]
        religion_pool = [Religion.generateRandomReligion() for _ in range(random.randint(5, 10))]
        factions = [World.generateRandomFactionForWorld(self, random.choice(culture_pool), random.choice(religion_pool)) for _ in range(random.randint(2, 5))]
        major_events = []
        return World(name, year, factions, major_events)


    def generateRandomFaction(self):
        name = random.choice(FACTION_NAMES)
        culture = Culture.generateRandomCulture()
        religion = Religion.generateRandomReligion()
        characters = []
        for _ in range(random.randint(20, 30)):
            characters.append(Character.generateRandomCharacter(self.year))
        leader = Character.generateRandomLeader()
        characters.append(leader)
        return Faction(name, culture, religion, leader, characters)
    
    def generateRandomFactionForWorld(self, culture, religion):
        name = random.choice(FACTION_NAMES)
        culture = culture
        religion = religion
        characters = []
        for _ in range(random.randint(20, 30)):
            characters.append(Character.generateRandomCharacter(self.year))
        leader = Character.generateRandomLeader(self.year)
        characters.append(leader)
        return Faction(name, culture, religion, leader, characters, 100)

    @staticmethod
    def generateCharacterBorn(current_year):
        fname = random.choice(NAMES)
        lname = random.choice(SURNAMES)
        birthdate = current_year
        age = 0
    
        traits = random.sample(list(CHARACTER_TRAITS.keys()), random.randint(1, 3))
        role_rank = random.randint(0, 2)
        match role_rank:
            case 2:
                role_title = random.choice(ROLE_2_TITLES)
            case 1:
                role_title = random.choice(ROLE_1_TITLES)
            case 0:
                role_title = random.choice(ROLE_0_TITLES)

        return Character(
            fname=fname,
            lname=lname,
            birthdate=birthdate,
            traits=traits,
            age = age,
            role_title=role_title,
            role_rank=role_rank
        )
    
    
    def describe(self):
        description = f"World Name: {self.name}\n"
        description += f"Year: {self.year}\n"
        description += f"Factions:\n"
        for faction in self.factions:
            description += f" - {faction.name}, Culture: {faction.culture.name}, Religion: {faction.religion.name}, Traditions: {', '.join(faction.culture.traditions)}\n"
        if self.major_events:
            description += "Major Events:\n"
            for event in self.major_events:
                description += f" - {event}\n"
        return description
    
    def advanceYear(self):
        self.year += 1
        self.addHistoricalEvent(f"\nYear {self.year} of {self.name}. --------------------")
        for faction in self.factions:
            faction.advanceYear(self)
            birth_chance = min((len(faction.characters) / 5) * random.randint(10, 15), 100)
            if birth_chance > 50:
                births = random.randint(1, 3)
                for _ in range(births):
                    new_char = World.generateCharacterBorn(self.year)
                    faction.characters.append(new_char)
                    self.addHistoricalEvent(f"In the faction of {faction.name}, a {new_char.role_title} named {new_char.fname} {new_char.lname} was born.")
            
        