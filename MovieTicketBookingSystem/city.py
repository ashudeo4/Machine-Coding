class City:
    def __init__(self,id, city):
        self.id = id
        self.city = city
        self.cinemaHall = []
        
    def addCinemaHall(self, cinemaHall):
        self.cinemaHall.append(cinemaHall)

