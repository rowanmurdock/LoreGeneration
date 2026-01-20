from world import World

if __name__ == "__main__":
    test = World("", 0, [], [])
    test_world = test.generateRandomWorld()
    print(test_world.factions[0].describe())
    for _ in range(10000):
        
        test_world.advanceYear()
        print(test_world.factions[0].leader.alive)
        print(len(test_world.factions[0].characters))


    
    
        
        