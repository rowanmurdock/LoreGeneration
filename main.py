from world import World

if __name__ == "__main__":
    test_world = World.generateRandomWorld()
    print(test_world.factions[0].describe())
    for _ in range(50):
        print("--------------------------------")
        print("Year:", test_world.getYear())
        test_world.advanceYear()
        
        