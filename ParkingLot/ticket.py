import datetime

class Ticket:
    def __init__(self, id, vehicleNumber):
        self.id = id
        self.vehicleNumber = vehicleNumber
        self.timeIn = datetime.datetime.now()
        self.timeOut = None
        self.price = 50

    def calculateCost(self):
        self.timeOut = datetime.datetime.now()
        self.price = 50
        return self.price