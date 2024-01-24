from django.urls import path

from payment_requests.views import PaymentRequestListView

urlpatterns = [
    path('', PaymentRequestListView.as_view(), name='payment_requests_list')
]
