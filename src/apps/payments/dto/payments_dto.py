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


@dataclass
class OrderDTO:
    id: int
    items: list[ItemDTO]
    total: int

    @classmethod
    def from_model(cls, order):
        items = [ItemDTO.from_model(item) for item in order.items.all()]
        total = sum(item.price for item in items) / 100
        return cls(id=order.id, items=items, total=total)
