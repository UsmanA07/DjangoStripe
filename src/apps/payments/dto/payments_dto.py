from dataclasses import dataclass


@dataclass
class ItemDTO:
    pk: int
    name: str
    description: str
    price: int

    @classmethod
    def from_model(cls, item):
        return cls(item.pk, item.name, item.description, item.price)

    @property
    def price_display(self) -> str:
        return f'{self.price / 100:.2f}'
