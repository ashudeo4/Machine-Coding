from abc import ABC, abstractmethod
from enum import Enum, auto

class VehicleType(Enum):
    FOURWHEELER = auto
    TWOWHEELER = auto

class Vehicle(ABC):
    def __init__(self, number):
        self.number =  number
    
    @abstractmethod
    def getNumber(self):
        return self.number
    
class FourWheelerVehicle(Vehicle):
    def __init__(self, number):
        super().__init__(number)
        self.type = VehicleType.FOURWHEELER
    
    def getNumber(self):
        return super().getNumber()

class TwoWheelerVehicle(Vehicle):
    def __init__(self, number):
        super().__init__(number)
        self.type = VehicleType.TWOWHEELER

    
    def getNumber(self):
        return super().getNumber()

    


        