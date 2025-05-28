import stripe
from django.conf import settings

from apps.payments.dto.payments_dto import ItemDTO, OrderDTO

stripe.api_key = settings.STRIPE_SECRET_KEY
domain_url = 'http://127.0.0.1:8000/'


class PaymentService:
    def __init__(self, repository):
        self.repository = repository

    def get_item_dto(self, item_id: int) -> ItemDTO:
        item = self.repository.get_by_id(item_id)
        return ItemDTO.from_model(item)

    @staticmethod
    def create_checkout_session(item_dto: ItemDTO) -> str:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price_data": {
                    "currency": "usd",
                    "unit_amount": int(item_dto.price),
                    "product_data": {
                        "name": item_dto.name,
                        "description": item_dto.description,
                    },
                },
                "quantity": 1,
            }],
            mode="payment",
            success_url="http://127.0.0.1:8000/success",
            cancel_url="http://127.0.0.1:8000/cancel",
        )
        return session.id


class OrderCheckoutService:
    def __init__(self, repository):
        self.repository = repository

    def get_order_dto(self, order_id: int) -> OrderDTO:
        order = self.repository.get_by_id(order_id)
        return order

    def create_checkout_session(self, order: OrderDTO) -> str:
        line_items = [
            {
                "price_data": {
                    "currency": "usd",
                    "unit_amount": item.price,
                    "product_data": {
                        "name": item.name,
                        "description": item.description,
                    },
                },
                "quantity": 1,
            }
            for item in order.items
        ]

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            mode="payment",
            success_url="http://127.0.0.1:8000/success",
            cancel_url="http://127.0.0.1:8000/cancel",
        )
        return session.id
