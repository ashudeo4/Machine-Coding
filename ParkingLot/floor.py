class Floor:
    def __init__(self, id, space):
        self.id = id
        self.spots = {}
        self.emptySpace = space
    
    def addSpot(self, spot):
        self.spots[spot.id] = spot
    
    def removeSpot(self, spotId):
        del self.spots[spotId]
    
    def decreaseEmptySpace(self):
        pass

    
    
        