from django.urls import path

from payment_requests.views import PaymentRequestListView, CheckingAccountFilerListView

urlpatterns = [
    path('', PaymentRequestListView.as_view(), name='payment_requests_list'),
    path('checking_account/', CheckingAccountFilerListView.as_view(), name='checking_account_list'),
]
