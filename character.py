import random
from traits import *
from names import *
from event import *

class Character:
    def __init__(self, fname, lname, birthdate, traits, role_title, role_rank, age):
        self.fname = fname
        self.lname = lname
        self.birthdate = birthdate
        self.deathdate = None
        self.traits = traits
        self.cause_of_death = None
        self.role_title = role_title
        self.role_rank = role_rank
        self.major_events = []
        self.age = age
        self.alive = True
        match self.role_rank:
            case 3:
                self.wealth = random.randint(1,50)
                self.power = random.randint(1,50)
                self.prestige = random.randint(1,50)
                ##1 is very moral or good, 100 is evil or aggressive
                self.morality = random.randint(1,100)
                ##1 is very low stress, 100 is very high stress
                self.stress = random.randint(30,90)
            case 2:
                self.wealth = random.randint(1,30)
                self.power = random.randint(1,30)
                self.prestige = random.randint(1,30)
                self.morality = random.randint(1,100)
                self.stress = random.randint(30,70)
            case 1:
                self.wealth = random.randint(1,10) 
                self.power = random.randint(1,10)
                self.prestige = random.randint(1,10)
                self.morality = random.randint(1,100)
                self.stress = random.randint(10,50)
            case _:
                self.wealth = random.randint(1,5)
                self.power = random.randint(1,5)
                self.prestige = random.randint(1,5)
                self.morality = random.randint(1,100)
                self.stress = random.randint(1,30)

    def describe(self):
        description = f"Name: {self.fname} {self.lname}\n"
        description += f"Birthdate: {self.birthdate}\n"
        description += f"Deathdate: {self.deathdate}\n"
        description += f"Role: {self.role_title} (Rank {self.role_rank})\n"
        description += f"Traits: {', '.join(self.traits)}\n"
        description += f"Cause of Death: {self.cause_of_death}\n"
        description += f"Wealth: {self.wealth}\n"
        description += f"Power: {self.power}\n"
        description += f"Prestige: {self.prestige}\n"
        description += f"Morality: {self.morality}\n"
        description += f"Stress: {self.stress}\n"
        if self.major_events:
            description += "Major Events:\n"
            for event in self.major_events:
                description += f" - {event}\n"
        return description
    
    @staticmethod
    def generateRandomCharacter(current_year):
        fname = random.choice(NAMES)
        lname = random.choice(SURNAMES)
        birthdate = random.randint(20, 80)
        age = birthdate - current_year
    
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
            role_title=role_title,
            role_rank=role_rank,
            age = age,
        )
    

    
    @staticmethod
    def generateRandomLeader(current_year):
        fname = random.choice(NAMES)
        lname = random.choice(SURNAMES)

        birthdate = random.randint(20, 80)
        age = birthdate - current_year 

    
        traits = random.sample(list(CHARACTER_TRAITS.keys()), random.randint(1, 3))
        role_rank = 3
        role_title = random.choice(ROLE_3_TITLES)

        return Character(
            fname=fname,
            lname=lname,
            birthdate=birthdate,
            traits=traits,
            role_title=role_title,
            role_rank=role_rank,
            age = age,
        )
    
    def ageUp(self, world):
        self.age += 1
        self.applyTraitEffects()
        self.clampStats()
        self.checkThresholds(world)
        

    def applyTraitEffects(self):
        for trait in self.traits:
            effects = CHARACTER_TRAITS.get(trait, {})
            for key, value in effects.items():
                if hasattr(self, key):
                    setattr(self, key, getattr(self, key) + value)


    def clampStats(self):
        for stat in ["power", "wealth", "prestige", "morality", "stress"]:
            value = getattr(self, stat)
            value = max(0, min(100, value))
            setattr(self, stat, value)

    def die(self, cause):
        self.deathdate = self.birthdate + self.age
        self.cause_of_death = cause
        self.alive = False

    def checkThresholds(self, world):
        if self.age >= 70:
            death_chance = random.randint(1, 100)
            if death_chance <= (self.age - 70) * 3:
                self.die("Old Age")
                world.addHistoricalEvent(f"{self.fname} {self.lname} has died of old age at {self.age}.")
        if self.stress >= 95:
            stress_chance = random.randint(1, 4)
            match stress_chance:
                case 1:
                    self.die("Heart Attack from Stress")
                    world.addHistoricalEvent(f"{self.fname} {self.lname} died of a heart attack caused by extreme stress at age {self.age}.")
                case 2:
                    self.die("Stroke from Stress")
                    world.addHistoricalEvent(f"{self.fname} {self.lname} died of a stroke caused by extreme stress at age {self.age}.")
                case 3:
                    self.major_events.append(Event("Suffered Severe Stress but Survived", "Stress", self.birthdate + self.age, self.birthdate + self.age))
                    self.stress -= 50
                    world.addHistoricalEvent(f"{self.fname} {self.lname} suffered severe stress but survived.")
                case 4:
                    self.major_events.append(Event("Suffered Severe Stress but Survived and Completely Recovered", "Stress", self.birthdate + self.age, self.birthdate + self.age))
                    self.stress -= 70
                    world.addHistoricalEvent(f"{self.fname} {self.lname} suffered severe stress but survived and completely recovered.")
        if self.role_rank < 2 and self.prestige >= 30:
            promotion_chance = random.randint(1, 100)
            if promotion_chance <= 50:
                self.role_rank += 1
                match self.role_rank:
                    case 1:
                        self.role_title = random.choice(ROLE_1_TITLES)
                    case 2:
                        self.role_title = random.choice(ROLE_2_TITLES)
                self.major_events.append(Event(f"Promoted to {self.role_title}", "Promotion", self.birthdate + self.age, self.birthdate + self.age))
                world.addHistoricalEvent(f"{self.fname} {self.lname} has been promoted to {self.role_title} at age {self.age}.")
        


        


    