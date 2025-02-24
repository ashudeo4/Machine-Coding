from enum import Enum, auto

class SpotType(Enum):
    FOURWHEELER = auto
    TWOWHEELER = auto

class Spot:
    def __init__(self, id, type, filled = False):
        self.id = id
        self.type = type
        self.filled = filled
    
    def clearSpot(self):
        self.filled = False
    
    def markSpot(self):
        self.filled = True



