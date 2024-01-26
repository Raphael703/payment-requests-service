from django.views.generic import ListView
from django_filters.views import FilterView

from payment_requests.filters import CheckingAccountFilterSet
from payment_requests.models import PaymentRequest, CheckingAccount
from payment_requests.sorters import SortableListMixin, SortField
from users.mixins import AdminRequiredMixin, CustomLoginRequiredMixin


class PaymentRequestListView(AdminRequiredMixin, ListView):
    model = PaymentRequest
    template_name = 'payment_requests/payment_request/list.html'
    context_object_name = 'payment_requests'

    paginate_by = 16

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_payment_requests_amount'] = self.model.objects.all().count()
        return context


class CheckingAccountFilerListView(CustomLoginRequiredMixin, SortableListMixin, FilterView):
    model = CheckingAccount
    template_name = 'payment_requests/checking_account/list.html'
    context_object_name = 'checking_accounts'

    paginate_by = 16
    default_sort_field = SortField('id')
    filterset_class = CheckingAccountFilterSet

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_checking_accounts_amount'] = self.model.objects.all().count()
        return context
