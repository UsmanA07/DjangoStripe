import stripe
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from config import settings


class PaymentsItemView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'payments/index.html'

    def get(self, request, pk):
        return Response(status=200)

class PaymentsBuyView(APIView):

    def get(self, request, pk):
        domain_url = 'http://127.0.0.1:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[{
                    "price_data": {
                        "currency": "usd",
                        "unit_amount": 2000,
                        "product_data": {
                            "name": "T-shirt",
                        },
                    },
                    "quantity": 1,
                }])
            print(checkout_session, 11111)
            return Response({'sessionId': checkout_session['id']})
        except Exception as e:
            return Response({'error': str(e)})