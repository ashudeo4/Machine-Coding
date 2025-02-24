from floor import Floor
from spot import Spot, SpotType
from ticket import Ticket
from vehicle import Vehicle, FourWheelerVehicle

class ParkingLotManager:
    strategy = None
    parkingLot= {}
    ticket = {}
    __emptySpace = 0
    def __init__(self, numberOfFloors, numberOfSpots) -> None:
        self.numberOfFloors = numberOfFloors
        self.numberOfSpots = numberOfSpots
        self.creatingParkingLot()

    
    def creatingParkingLot(self):
        for floorId in range(self.numberOfFloors):
            floor = Floor(floorId, self.numberOfSpots)

            for spotId in range(self.numberOfSpots):
                spot = Spot(spotId, SpotType.FOURWHEELER)
                floor.addSpot(spot)
            self.parkingLot[floorId] = floor
        self.__emptySpace = self.numberOfFloors * self.numberOfSpots
    
    def addVehicle(self, vehicle):
        # Find a parking spot
        # generate Ticket
        # park it and return ticket id
        floorId, spotId = self.findAParkingSpot()
        if floorId == -1 and spotId == -1:
            print("Parking Lot is full")
            return
        ticketId = f"{floorId},{spotId}"
        ticket = Ticket(ticketId, vehicle.number)
        self.ticket[ticketId] = ticket
        self.parkingLot[floorId].spots[spotId].markSpot()
        self.__emptySpace -=1
        return ticket.id
    
    def removeVehicle(self, ticketId):
        ticket = self.ticket[ticketId]
        ticket.calculateCost()
        floorId, spotId = map(int, ticket.id.split(","))
        self.parkingLot[floorId].spots[spotId].clearSpot()
        self.__emptySpace +=1
        return ticket.price
    


    def findAParkingSpot(self):
        for floorId in range(self.numberOfFloors):
            for spotId in range(self.numberOfSpots):
                if self.parkingLot[floorId].spots[spotId].filled == False:
                    return (floorId, spotId)
        return (-1, -1)
    
    def getEmptySpaces(self):
        return self.__emptySpace


parkingLot = ParkingLotManager(10, 10)


vehicle1 = FourWheelerVehicle("UP32NY7162")
vehicle2 = FourWheelerVehicle("UP32NY7161")
vehicle3 = FourWheelerVehicle("UP32NY7164")
vehicle4 = FourWheelerVehicle("UP32NY7165")
vehicle5 =  FourWheelerVehicle("UP32NY1234")
print("Five vechicle came in")





ticket1 = parkingLot.addVehicle(vehicle1)
ticket2 = parkingLot.addVehicle(vehicle2)
ticket3 = parkingLot.addVehicle(vehicle3)
ticket4 = parkingLot.addVehicle(vehicle4)
print("Four vehicle parked")
print("Empty spaces", parkingLot.getEmptySpaces())
parkingLot.removeVehicle(ticket3)
print("Vechile 3 have been removed")
print("Empty space now",parkingLot.getEmptySpaces())

ticket5 = parkingLot.addVehicle(vehicle5)
print("Vechicle 5 is parked")
print("Empty space now",parkingLot.getEmptySpaces())



print(ticket1,ticket2,ticket3,ticket4,ticket5)


