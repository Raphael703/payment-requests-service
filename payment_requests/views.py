from django.views.generic import ListView

from payment_requests.models import PaymentRequest


class PaymentRequestListView(ListView):
    model = PaymentRequest
    template_name = 'payment_requests/list.html'
    context_object_name = 'payment_requests'

    paginate_by = 16
