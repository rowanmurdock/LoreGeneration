import random
from names import *
from traits import *

class Religion:
    def __init__(self, name, deities, traditions):
        self.name = name
        self.deities = deities
        self.traditions = traditions

    @staticmethod
    def generate_random_religion():
        name = random.choice(RELIGION_NAMES)
        deities = random.sample(GOD_NAMES, random.randint(1, 3))
        traditions = random.sample(list(RELIGIOUS_TRADITIONS.keys()), random.randint(1, 5))
        return Religion(name, deities, traditions)