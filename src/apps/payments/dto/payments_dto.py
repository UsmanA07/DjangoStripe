from dataclasses import dataclass


@dataclass
class ItemDTO:
    name: str
    description: str
    price: int

    @classmethod
    def from_model(cls, item):
        return cls(item.name, item.description, item.price)
