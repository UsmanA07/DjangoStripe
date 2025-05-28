from django.urls import path, include
from api.v1.payments.views import PaymentsItemView, PaymentsBuyView, OrderBuyView, OrderItemView

urlpatterns = [
    path('item/<int:pk>/', PaymentsItemView.as_view(), name='item-id'),
    path('buy/<int:pk>/', PaymentsBuyView.as_view(), name='buy-id'),
    path("order/buy/<int:pk>/", OrderBuyView.as_view()),
    path("order/item/<int:pk>/", OrderItemView.as_view()),
]
