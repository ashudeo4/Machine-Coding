class User:
    def __init__(self, userId=0, userName="", drivingLicense=""):
        self._userId = userId
        self._username = userName
        self._drivingLicense = drivingLicense

    def getUserId(self):
        return self._userId
    
    def setUserId(self, value):
        self._userId = value

    def getUserName(self):
        return self._username

    def setUserName(self, value):
        self._username = value

    def getDrivingLicense(self):
        return self._drivingLicense

    def setDrivingLicense(self, value):
        self._drivingLicense = value