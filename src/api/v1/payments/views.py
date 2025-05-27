import stripe
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from apps.payments.dto.payments_dto import ItemDTO
from apps.payments.repositories.repositories import ImplItemRepository
from apps.payments.services.payment_services import PaymentService
from config import settings


class PaymentsItemView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'payments/index.html'

    def get(self, request, pk):
        return Response(status=200)


class PaymentsBuyView(APIView):
    services = PaymentService(ImplItemRepository())

    def get(self, request, pk):
        try:
            item_dto = self.services.get_item_dto(pk)
            print(item_dto)
            session_id = self.services.create_checkout_session(item_dto)
            print(session_id)
            return Response({'session_id': session_id})
        except Exception as e:
            return Response({'error': str(e)})
