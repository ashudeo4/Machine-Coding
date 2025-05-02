from enum import Enum

class VehicleType(Enum):
    CAR = "Car"
    BIKE = "Bike"
    TRUCK = "TRUCK"
    
class Status(Enum):
    AVAILABLE = "Available"
    RENTED = "Rented"
    MAINTENANCE = "Maintenance"
    

class Vehicle:
    def __init__(self,
                 vehicleId=0,
                 vehicleNumber=0,
                 vehicleType=0,
                 companyName=0,
                 modelName=0,
                 kmDriven=0,
                 manufacturingDate=0,
                 average=0,
                 cc=0,
                 dailyRentalCost=0,
                 hourlyRentalCost=0,
                 noOfSeat=0,
                 status=0):
        self._vehicleId = vehicleId
        self._vehicleNumber = vehicleNumber
        self._vehicleType = vehicleType
        self._companyName = companyName
        self._modelName = modelName
        self._kmDriven = kmDriven
        self._manufacturingDate = manufacturingDate
        self._average = average
        self._cc = cc
        self._dailyRentalCost = dailyRentalCost
        self._hourlyRentalCost = hourlyRentalCost
        self._noOfSeat = noOfSeat
        self._status = status


    @property
    def vehicleId(self):
        return self._vehicleId

    def vehicleId(self, value):
        self._vehicleId = value

    @property
    def vehicleNumber(self):
        return self._vehicleNumber

    def vehicleNumber(self, value):
        self._vehicleNumber = value

    @property
    def vehicleType(self):
        return self._vehicleType

    def vehicleType(self, value):
        self._vehicleType = value

    @property
    def companyName(self):
        return self._companyName

    @companyName.setter
    def companyName(self, value):
        self._companyName = value

    @property
    def modelName(self):
        return self._modelName

    @modelName.setter
    def modelName(self, value):
        self._modelName = value

    @property
    def kmDriven(self):
        return self._kmDriven

    @kmDriven.setter
    def kmDriven(self, value):
        self._kmDriven = value

    @property
    def manufacturingDate(self):
        return self._manufacturingDate

    @manufacturingDate.setter
    def manufacturingDate(self, value):
        self._manufacturingDate = value

    @property
    def average(self):
        return self._average

    @average.setter
    def average(self, value):
        self._average = value

    @property
    def cc(self):
        return self._cc

    @cc.setter
    def cc(self, value):
        self._cc = value

    @property
    def dailyRentalCost(self):
        return self._dailyRentalCost

    @dailyRentalCost.setter
    def dailyRentalCost(self, value):
        self._dailyRentalCost = value

    @property
    def hourlyRentalCost(self):
        return self._hourlyRentalCost

    @hourlyRentalCost.setter
    def hourlyRentalCost(self, value):
        self._hourlyRentalCost = value

    @property
    def noOfSeat(self):
        return self._noOfSeat

    @noOfSeat.setter
    def noOfSeat(self, value):
        self._noOfSeat = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value