from dataclasses import dataclass
    
@dataclass
class Store:
    store_id: int
    store_name: str
    zone: str
    items: list[str]

    def has_item(self, item_name: str) -> bool:
        return item_name in self.items
    
