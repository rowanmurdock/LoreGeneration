from faction import Faction
from world import World

if __name__ == "__main__":
    test_world = World.generateRandomWorld()
    print(test_world.describe())