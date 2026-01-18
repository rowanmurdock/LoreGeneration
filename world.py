import random
from names import *
from faction import Faction
from culture import Culture
from religion import Religion


class World:
    def __init__(self, name, year, factions, major_events):
        self.name = name
        self.year = year
        self.factions = factions
        self.major_events = major_events

    def getYear(self):
        return self.year
    
    def factionEnds(self, faction):
        self.major_events.append(f"The faction of {faction.name} has ended.")
        self.factions.remove(faction)

    @staticmethod
    def generateRandomWorld():
        name = random.choice(WORLD_NAMES)
        year = 100
        culture_pool = [Culture.generateRandomCulture() for _ in range(random.randint(5, 10))]
        religion_pool = [Religion.generateRandomReligion() for _ in range(random.randint(5, 10))]
        factions = [Faction.generateRandomFactionForWorld(random.choice(culture_pool), random.choice(religion_pool)) for _ in range(random.randint(2, 5))]
        major_events = []
        return World(name, year, factions, major_events)
    
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