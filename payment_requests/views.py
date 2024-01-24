from django.views.generic import ListView

from payment_requests.models import PaymentRequest, CheckingAccount
from payment_requests.sorters import SortableListMixin, SortField


class PaymentRequestListView(ListView):
    model = PaymentRequest
    template_name = 'payment_requests/payment_request/list.html'
    context_object_name = 'payment_requests'

    paginate_by = 16


class CheckingAccountListView(SortableListMixin, ListView):
    model = CheckingAccount
    template_name = 'payment_requests/checking_account/list.html'
    context_object_name = 'payment_requests'
    paginate_by = 16
    default_sort_field = SortField('id')
