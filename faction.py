import random
from names import *
from character import Character

class Faction:
    def __init__(self, name, culture, religion, leader, characters):
        self.name = name
        self.culture = culture
        self.religion = religion
        self.leader = leader
        self.characters = characters
        self.population = len(characters) * 1000 * random.randint(1,10)
        self.resources = 50
        self.war_pressure = 0
        self.stability = 100
        self.religious_tension = 0
        self.major_events = []

    def describe(self):
        description = f"Faction Name: {self.name}\n"
        description += f"Culture: {self.culture}\n"
        description += f"Religion: {self.religion}\n"
        description += f"Leader: {self.leader.name}\n"
        description += f"Population: {self.population}\n"
        description += f"Resources: {self.resources}\n"
        description += f"War Pressure: {self.war_pressure}\n"
        description += f"Stability: {self.stability}\n"
        description += f"Religious Tension: {self.religious_tension}\n"
        if self.major_events:
            description += "Major Events:\n"
            for event in self.major_events:
                description += f" - {event}\n"
        return description
    
    def generate_random_faction(self):
        name = random.choice(FACTION_NAMES)
        culture = random.choice(CULTURE_NAMES)
        religion = random.choice(RELIGION_NAMES)
        characters = []
        for i in range(random.randint(10, 30)):
            characters.append(Character.generate_random_character())
        leader = max(characters, key=lambda c: c.role_rank)
        return Faction(name, culture, religion, leader, characters)
    
        

  