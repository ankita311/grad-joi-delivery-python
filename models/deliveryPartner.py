from dataclasses import dataclass
from typing import List

@dataclass
class Delivery:
    time: int        # in minutes
    distance: float  # in kilometers

@dataclass
class DeliveryPartner:
    id: int
    name: str
    deliveries: List[Delivery]

    def total_deliveries(self) -> int:
        return len(self.deliveries)

