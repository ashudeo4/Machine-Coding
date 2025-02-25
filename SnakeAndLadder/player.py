class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.position = 0
        
    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position
