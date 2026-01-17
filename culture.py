from names import *
from traits import *
import random

class Culture:
    def __init__(self, name, traditions):
        self.name = name
        self.traditions = traditions

    @staticmethod
    def generate_random_culture():
        name = random.choice(CULTURE_NAMES)
        traditions = random.sample(list(CULTURE_TRAITS.keys()), random.randint(1, 5))
        return Culture(name, traditions)