from Product.Vehicle import Vehicle
from Reservation import Reservation
from User import User
from VehicleInventoryManagement import VehicleInventoryManagement
from Location import Location

class Store:
    def __init__(self, storeId=0, inventoryManagement=0, storeLocation=0):
        self.storeId = storeId
        self.inventoryManagement = inventoryManagement
        self.storeLocation = storeLocation
        self.reservations = []


    def setStoreId(self, value):
        self.storeId = value

    def getVehicles(self, vehicleType):
        return self.inventoryManagement.getVehicles()

    def setVehicles(self, vehicles):
        self.inventoryManagement = VehicleInventoryManagement(vehicles)

    def createReservation(self, vehicle: Vehicle, user: User):
        reservation: Reservation = Reservation(self)
        reservation.createReserve(user, vehicle)
        self.reservations.append(reservation)
        return reservation
    
    def completeReservation(self, reservationId):
        return True