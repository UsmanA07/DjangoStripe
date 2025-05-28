from apps.payments.models import Item, Order
from django.shortcuts import get_object_or_404
from abc import ABC, abstractmethod
from apps.payments.dto.payments_dto import ItemDTO, OrderDTO


class ItemRepository(ABC):
    @staticmethod
    @abstractmethod
    def get_by_id(pk: int) -> ItemDTO:
        pass


class OrderRepository(ABC):
    @staticmethod
    @abstractmethod
    def get_by_id(pk: int) -> OrderDTO:
        pass


class ImplItemRepository:
    @staticmethod
    def get_by_id(pk: int) -> ItemDTO:
        item = get_object_or_404(Item, pk=pk)
        return ItemDTO.from_model(item)


class ImplOrderRepository:
    @staticmethod
    def get_by_id(pk: int) -> OrderDTO:
        order = get_object_or_404(Order, pk=pk)
        return OrderDTO.from_model(order)
