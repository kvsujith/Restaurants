from enum import Enum


class PaymentStatus(Enum):
    invoice_generated = 1
    paid = 2
    due = 3
