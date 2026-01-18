import random

class Event:
    def __init__(self, name, event_type, start_year):
        self.name = name
        self.event_type = event_type
        self.start_year = start_year
        self.end_year = None
        self.active = True

    def progress(self):
        pass

    def end(self, year):
        self.end_year = year
        self.active = False


class War(Event):
    def __init__(self, attacker, defender, start_year):
        name = f"War between {attacker.name} and {defender.name}"
        super().__init__(name, "War", start_year)

        self.attacker = attacker
        self.defender = defender
        self.duration = 0

    def progress(self):
        self.duration += 1

        self.attacker.resources -= 3
        self.defender.resources -= 3

        self.attacker.stability -= 2
        self.defender.stability -= 2

        self.defender.population -= self.attacker.getMilitaryStrength() * 10 * random.randint(1, 3)
        self.attacker.population -= self.defender.getMilitaryStrength() * 10 * random.randint(1, 3)

        if self.attacker.resources <= 0 or self.defender.resources <= 0:
            self.end(self.start_year + self.duration)
        if self.attacker.population <= 0 or self.defender.population <= 0:
            self.end(self.start_year + self.duration)
        if self.duration >= random.randint(10, 15):
            self.end(self.start_year + self.duration)