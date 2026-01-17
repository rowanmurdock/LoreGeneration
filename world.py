class World:
    def __init__(self, name, year, factions, major_events):
        self.name = name
        self.year = year
        self.factions = factions
        self.major_events = major_events

    def get_year(self):
        return self.year
    
    