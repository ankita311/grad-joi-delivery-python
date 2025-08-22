from enum import Enum

class OrderStatus(Enum):
    CREATED = "created"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    REJECTED = "rejected"
