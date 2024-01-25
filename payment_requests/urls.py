from django.urls import path, include

from payment_requests.views import PaymentRequestListView, CheckingAccountFilerListView

urlpatterns = [
    path('payment-request-list/', PaymentRequestListView.as_view(),
         name='payment_requests_list'),
    path('checking-account-list/', CheckingAccountFilerListView.as_view(),
         name='checking_account_list'),
    path('api/v1/', include('payment_requests.api.urls')),
]
