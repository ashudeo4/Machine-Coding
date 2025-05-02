from Location import Location


class VehicleRentalSystem:
    def __init__(self, stores, users):
        self.storeList = stores
        self.userList = users
    
    def getStore(self, location: Location):
        return self.storeList[0]
    
    # AddUsers
    # removeUsers
    # add stores
    # remove stores