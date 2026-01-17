import random
from names import *
from character import Character
from culture import Culture
from religion import Religion

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
        description += f"Culture: {self.culture.name}\n"
        description += f"Traditions: {', '.join(self.culture.traditions)}\n"
        description += f"Religion: {self.religion.name}\n"
        description += f"Leader: {self.leader.name}\n"
        description += f"Population: {self.population}\n"
        description += f"Resources: {self.resources}\n"
        description += f"War Pressure: {self.war_pressure}\n"
        description += f"Stability: {self.stability}\n"
        description += f"Religious Tension: {self.religious_tension}\n"
        if self.characters:
            description += "Notable Characters:\n"
            for char in self.characters[:10]:
                description += f" - {char.name}, Role: {char.role_title}\n"
        if self.major_events:
            description += "Major Events:\n"
            for event in self.major_events:
                description += f" - {event}\n"
        return description
    
    @staticmethod
    def generate_random_faction():
        name = random.choice(FACTION_NAMES)
        culture = Culture.generate_random_culture()
        religion = Religion.generate_random_religion()
        characters = []
        for i in range(random.randint(10, 30)):
            characters.append(Character.generate_random_character())
        leader = max(characters, key=lambda c: c.role_rank)
        return Faction(name, culture, religion, leader, characters)
    
        

  