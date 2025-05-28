from django.urls import path, include
from api.v1.payments.views import PaymentsItemView, PaymentsBuyView

urlpatterns = [
    path('item/<int:pk>/', PaymentsItemView.as_view(), name='item-id'),
    path('buy/<int:pk>/', PaymentsBuyView.as_view(), name='buy-id'),
]
