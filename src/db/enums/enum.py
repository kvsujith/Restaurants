from enum import Enum


class TagType(Enum):
    restaurant_tag = 1
    dish_tag = 2


class OrderStatus(Enum):
    order_placed = 1
    served = 2
    delivered = 3


class OrderType(Enum):
    take_away = 1
    dine_in = 2


class PaymentStatus(Enum):
    invoice_generated = 1
    paid = 2
    due = 3
