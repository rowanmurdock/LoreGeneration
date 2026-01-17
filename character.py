import random

class Character:
    def __init__(self, name, birthdate, traits, role_title, role_rank):
        self.name = name
        self.birthdate = birthdate
        self.deathdate = None
        self.traits = traits
        self.cause_of_death = None
        self.role_title = role_title
        self.role_rank = role_rank
        self.major_events = []
        match self.role_rank:
            case 3:
                self.wealth = random.randint(1,50)
                self.power = random.randint(1,50)
                self.prestige = random.randint(1,50)
                ##1 is very moral or good, 100 is evil or aggressive
                self.morality = random.randint(1,100)
                ##1 is very low stress, 100 is very high stress
                self.stress = random.randint(50,90)
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
        description = f"Name: {self.name}\n"
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
        


    