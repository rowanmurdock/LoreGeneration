import random
from event import *
from names import *
from character import Character
from culture import Culture
from religion import Religion
from traits import *

class Faction:
    def __init__(self, name, culture, religion, leader, characters, startDate):
        self.name = name
        self.culture = culture
        self.religion = religion
        self.leader = leader
        self.characters = characters
        self.population = len(characters) * 100 * random.randint(1,10)
        self.resources = 50
        self.war_pressure = 0
        self.stability = 100
        self.religious_tension = 0
        self.major_events = []
        self.startDate = startDate
        self.age = 0

    def describe(self):
        description = f"Faction Name: {self.name}\n"
        description += f"Culture: {self.culture.name}\n"
        description += f"Traditions: {', '.join(self.culture.traditions)}\n"
        description += f"Religion: {self.religion.name}\n"
        description += f"Beliefs: {', '.join(self.religion.traditions)}\n"
        description += f"Leader: {self.leader.name}, Title: {self.leader.role_title}, Traits: {', '.join(self.leader.traits)}\n"
        description += f"Population: {self.population}\n"
        description += f"Resources: {self.resources}\n"
        description += f"War Pressure: {self.war_pressure}\n"
        description += f"Stability: {self.stability}\n"
        description += f"Religious Tension: {self.religious_tension}\n"
        description += f"Military Strength: {self.getMilitaryStrength()}\n"
        if self.characters:
            description += "Notable Characters:\n"
            for char in self.characters[:10]:
                description += f" - {char.name}, Role: {char.role_title}, Traits: {', '.join(char.traits)}\n"
        if self.major_events:
            description += "Major Events:\n"
            for event in self.major_events:
                description += f" - {event}\n"
        return description
    
    def applyCultureAndReligionEffects(self):
        for trait in self.culture.traditions:
            if trait in CULTURE_TRAITS:
                for key, value in CULTURE_TRAITS[trait].items():
                    setattr(self, key, getattr(self, key) + value)
        for trait in self.religion.traditions:
            if trait in RELIGIOUS_TRADITIONS:
                for key, value in RELIGIOUS_TRADITIONS[trait].items():
                    setattr(self, key, getattr(self, key) + value)

    def clampStats(self):
        for stat in ["resources", "war_pressure", "stability", "religious_tension"]:
            value = getattr(self, stat)
            value = max(0, min(100, value))
            setattr(self, stat, value)

    def advanceYear(self):
        self.age += 1
        self.applyCultureAndReligionEffects()
        self.clampStats()
        for char in self.characters:
            char.ageUp()
    
    def getMilitaryStrength(self):
        base_strength = self.population // 1000
        for char in self.characters:
            if any(trait in char.traits for trait in ["military genius", "brave", "ambitious"]):
                base_strength += 5
            if char.power > 50 and char.power <= 70:
                base_strength += 5
            elif char.power > 70 and char.power <= 90:
                base_strength += 10
            elif char.power > 90:
                base_strength += 20
            else:
                base_strength += 0
        return base_strength
    
    def factionEnds(self):
        self.major_events.append(Event(f"The faction of {self.name} has ended.", "Faction End", self.startDate + self.age, self.startDate + self.age))

    def checkThresholds(self):
        if self.stability <= 0:
            self.factionEnds()
        if self.population <= 0:
            self.factionEnds()

    
    @staticmethod
    def generateRandomFaction():
        name = random.choice(FACTION_NAMES)
        culture = Culture.generateRandomCulture()
        religion = Religion.generateRandomReligion()
        characters = []
        for i in range(random.randint(10, 30)):
            characters.append(Character.generateRandomCharacter())
        leader = Character.generateRandomLeader()
        return Faction(name, culture, religion, leader, characters)
    
    @staticmethod
    def generateRandomFactionForWorld(culture, religion):
        name = random.choice(FACTION_NAMES)
        culture = culture
        religion = religion
        characters = []
        for i in range(random.randint(10, 30)):
            characters.append(Character.generateRandomCharacter())
        leader = Character.generateRandomLeader()
        return Faction(name, culture, religion, leader, characters)
    

    
        

  