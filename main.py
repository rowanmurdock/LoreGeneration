import names
from names import *
import random
from names import ROLE_3_TITLES
from names import ROLE_2_TITLES
from names import ROLE_1_TITLES
from names import ROLE_0_TITLES
from traits import TRAITS
from character import Character

from names import NAMES

def generate_random_character():
    name = random.choice(NAMES)
    birthdate = random.randint(0, 80)
    deathdate = None
    cause_of_death = None

    traits = random.sample(TRAITS, random.randint(1, 3))
    role_rank = random.randint(0, 3)
    match role_rank:
        case 3:
            role_title = random.choice(ROLE_3_TITLES)
        case 2:
            role_title = random.choice(ROLE_2_TITLES)
        case 1:
            role_title = random.choice(ROLE_1_TITLES)
        case 0:
            role_title = random.choice(ROLE_0_TITLES)

    return Character(
        name=name,
        birthdate=birthdate,
        deathdate=deathdate,
        traits=traits,
        cause_of_death=cause_of_death,
        role_title=role_title,
        role_rank=role_rank
    )
if __name__ == "__main__":
    character = generate_random_character()
    print(character.describe())