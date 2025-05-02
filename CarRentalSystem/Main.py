from Bill import Bill
from Location import Location
from Payment import Payment
from Product.Car import Car
from Product.Vehicle import Vehicle, VehicleType
from Reservation import Reservation
from Store import Store
from User import User
from VehicleRentalSystem import VehicleRentalSystem


class Main:
    def main(self):
        users = self.addUsers()
        vehicles = self.addVehicles()
        stores = self.addStores(vehicles)

        rentalSystem: VehicleRentalSystem = VehicleRentalSystem(stores, users)

        #0. User comes
        user: User = users[0]
        #1. User search store based on location
        location: Location = Location(403013, "Banglore", "Karnataka", "India")
        store: Store = rentalSystem.getStore(location)

        #2. get all vehicles you are interested in(based upon different filters)
        storeVehicles = store.getVehicles(VehicleType.CAR)

        #3. Reserving the particular vehicle
        reservation: Reservation = store.createReservation(storeVehicles[0], users[0])

        #4. Generate the bill
        bill: Bill = Bill(reservation)

        #5. Make Payment
        payment: Payment = Payment()
        payment.payBill(bill)

        #6. trip completed, submit the vehivle and close the reservation
        store.completeReservation(reservation.reservationId)


    def addUsers(self):
        users = []
        user1 = User()
        user1.setUserId(1)

        users.append(user1)
        return users
    
    def addVehicles(self):
        vehicles = []
        vehicle1 = Car()
        vehicle1.vehicleId(1)
        vehicle1.vehicleType(VehicleType.CAR)

        vehicle2: Vehicle = Car()
        vehicle2.vehicleId(2)
        vehicle2.vehicleType(VehicleType.CAR)

        vehicles.append(vehicle1)
        vehicles.append(vehicle2)

        return vehicles
    
    def addStores(self,vehicles):
        stores = []
        store1 = Store()
        store1.setStoreId(1)
        store1.setVehicles(vehicles)

        stores.append(store1)

        return stores
    


main = Main()

main.main()