from django.urls import path

from payment_requests.api.viewsets import InvoiceStatusAPIView, InvoiceCreateAPIView

urlpatterns = [
    path('get-invoice-status/<uuid:invoice_id>/', InvoiceStatusAPIView.as_view(),
         name='get_invoice_status'),
    path('create-invoice/<int:payment_type>/<str:amount>', InvoiceCreateAPIView.as_view(),
         name='create_invoice'),
]
