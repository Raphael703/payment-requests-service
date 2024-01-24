import django_filters
from django import forms
from django.utils.translation import gettext_lazy as _
from django_filters import FilterSet
from django_filters.widgets import RangeWidget

from payment_requests.models import CheckingAccount


class CheckingAccountFilterSet(FilterSet):
    owner_name = django_filters.CharFilter(
        lookup_expr='icontains',
        label=_('ФИО владельца'),
        widget=forms.TextInput(attrs={'placeholder': _('ФИО владельца содержит')})
    )
    phone_number = django_filters.CharFilter(
        lookup_expr='icontains',
        label=_('Номер телефона'),
        widget=forms.TextInput(attrs={'placeholder': _('Номер телефона содержит')})
    )
    limit = django_filters.RangeFilter(
        label='Лимит',
        widget=RangeWidget(attrs={
            'placeholder': 'Введите минимальный лимит и максимальный лимит',
        }),
    )

    class Meta:
        model = CheckingAccount
        fields = {
            'payment_type': ['exact'],
            'card_type': ['exact'],
            'account_type': ['exact'],
        }
