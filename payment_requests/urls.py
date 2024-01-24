from django.urls import path

from payment_requests.views import PaymentRequestListView, CheckingAccountListView

urlpatterns = [
    path('', PaymentRequestListView.as_view(), name='payment_requests_list'),
    path('checking_account/', CheckingAccountListView.as_view(), name='checking_account_list'),
]
