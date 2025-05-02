from enum import Enum

class PaymentMode(Enum):
    CASH = "CASH"
    ONLINE = "ONLINE"
class PaymentDetails:
    def __init__(self, paymentId, amountPaid, dateOfPayment,
                 isRefundable, paymentMode: PaymentMode):
        self.paymentId = paymentId
        self.amountPaid = amountPaid
        self.dateOfPayment = dateOfPayment
        self.isRefundable = isRefundable
        self.paymentMode = paymentMode