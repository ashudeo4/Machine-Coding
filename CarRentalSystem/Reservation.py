from Location import Location
from Product.Vehicle import Vehicle
from datetime import date as Date
from enum import Enum
from User import User

class ReservationType(Enum):
    HOURLY = "HOURLY"
    DAILY = "DAILY"

class ReservationStatus(Enum):
    SCHEDULED = "SCHEDULED"
    INPROGRESS = "INPROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"

class Reservation:
    def __init__(self, reservationId,
                user=0,
                vehicle=0,
                bookingDate=0,
                bookedFrom=0,
                bookedTo=0,
                pickUpLocation=0,
                dropLocation= 0,
                reservationType=0,
                status=0,
                location=0):
        pass
    
    def createReserve(self, user: User, vehicle: Vehicle):
        self.reservationId = "123"
        self.user = user
        self.vehicle = vehicle
        self.reservationType = ReservationType.DAILY
        self.status = ReservationStatus.SCHEDULED

        return self.reservationId