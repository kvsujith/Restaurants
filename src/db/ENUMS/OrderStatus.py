from enum import Enum


class OrderStatus(Enum):
    order_placed = 1
    served = 2
    delivered = 3