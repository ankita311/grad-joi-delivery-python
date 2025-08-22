from dataclasses import dataclass

@dataclass(frozen=True)
class DistanceMap:
    zone_to: str
    zone_from: str
    distance: int

   
