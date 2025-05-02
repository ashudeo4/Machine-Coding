class cinemaHall:
    def __init__(self, id, name, city):
        self.id = id
        self.name = name
        self.city = city
        self.shows = []
        
    def addShows(self, show):
        self.shows.append(show)
