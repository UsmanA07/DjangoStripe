import stripe
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from apps.payments.dto.payments_dto import ItemDTO
from apps.payments.repositories.repositories import ImplItemRepository, OrderRepository, ImplOrderRepository
from apps.payments.services.payment_services import PaymentService, OrderCheckoutService
from config import settings


class PaymentsItemView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'payments/index.html'
    service = PaymentService(ImplItemRepository())

    def get(self, request, pk):
        item_dto = self.service.get_item_dto(pk)
        print(item_dto)

        return Response({
            'item': item_dto,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY
        })


class PaymentsBuyView(APIView):
    services = PaymentService(ImplItemRepository())

    def get(self, request, pk):
        try:
            item_dto = self.services.get_item_dto(pk)
            session_id = self.services.create_checkout_session(item_dto)
            return Response({'session_id': session_id})
        except Exception as e:
            return Response({'error': str(e)}, status=400)


class OrderPaymentService:
    pass


class OrderBuyView(APIView):
    service = OrderCheckoutService(ImplOrderRepository())

    def get(self, request, pk):
        try:
            order = self.service.get_order_dto(pk)
            session_id = self.service.create_checkout_session(order)
            return Response({'session_id': session_id})
        except Exception as e:
            return Response({'error': str(e)}, status=400)


class OrderItemView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'payments/order.html'
    service = OrderCheckoutService(ImplOrderRepository())

    def get(self, request, pk):
        order_dto = self.service.get_order_dto(pk)
        print(order_dto)

        return Response({
            'order': order_dto,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY
        })
