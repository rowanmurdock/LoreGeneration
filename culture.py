from names import *
import random

class Culture:
    def __init__(self, name, traditions):
        self.name = name
        self.traditions = traditions

    def generate_random_culture(self):
        name = random.choice(CULTURE_NAMES)
        traditions = random.sample(TRADITIONS, random.randint(1, 5))
        return Culture(name, traditions)