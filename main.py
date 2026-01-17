from names import *
import random
from traits import *
from character import Character


if __name__ == "__main__":
    character = generate_random_character()
    print(character.describe())