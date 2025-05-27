from apps.payments.models import Item
from django.shortcuts import get_object_or_404
from abc import ABC, abstractmethod
from apps.payments.dto.payments_dto import ItemDTO


class ItemRepository(ABC):
    @staticmethod
    @abstractmethod
    def get_by_id(pk: int) -> Item:
        pass


class ImplItemRepository:
    @staticmethod
    def get_by_id(pk: int) -> ItemDTO:
        item = get_object_or_404(Item, pk=pk)
        return ItemDTO.from_model(item)
