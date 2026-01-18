import random
from names import *
from faction import Faction
from culture import Culture
from religion import Religion
from event import *


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
    
    def advanceYear(self):
        self.year += 1
        for faction in self.factions:
            faction.advanceYear()