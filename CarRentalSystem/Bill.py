from Reservation import Reservation


class Bill:
    def __init__(self, reservation: Reservation, totalBillAmount=0, isBillPaid=True):
        self.reservation = reservation
        self.totalBillAmount = totalBillAmount
        self.isBillPaid = isBillPaid

    def computeBillAmount(self):
        return 100.0
