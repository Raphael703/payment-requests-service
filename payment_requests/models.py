import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from payment_requests.consts import PAYMENT_REQUEST_STATUS, PAYMENT_TYPES, \
    CARD_TYPES, CHECKING_ACCOUNT_TYPES


class CheckingAccount(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payment_type = models.PositiveSmallIntegerField(
        verbose_name=_('Тип платежа'),
        choices=PAYMENT_TYPES
    )
    card_type = models.PositiveSmallIntegerField(
        verbose_name=_('Тип карты'),
        choices=CARD_TYPES
    )
    account_type = models.PositiveSmallIntegerField(
        verbose_name=_('Тип счёта'),
        choices=CHECKING_ACCOUNT_TYPES
    )
    owner_name = models.CharField(
        verbose_name=_('ФИО владельца'),
        max_length=255
    )
    phone_number = PhoneNumberField(
        verbose_name=_('Номер телефона'),
        blank=True
    )
    limit = models.DecimalField(
        verbose_name=_('Лимит'),
        max_digits=10, decimal_places=2
    )

    def __str__(self):
        return f'Реквизиты # {self.id} - {self.owner_name}'

    class Meta:
        verbose_name = _('Реквизит')
        verbose_name_plural = _('Реквизиты')


class PaymentRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(
        verbose_name=_('Сумма'),
        max_digits=16, decimal_places=2
    )
    account = models.ForeignKey(
        verbose_name=_('Реквизиты'),
        to=CheckingAccount,
        on_delete=models.CASCADE
    )
    status = models.PositiveSmallIntegerField(
        verbose_name=_('Статус'),
        choices=PAYMENT_REQUEST_STATUS
    )

    def __str__(self):
        return f'Заявка # {self.id} - Сумма: {self.amount}'

    class Meta:
        verbose_name = _('Заявка на оплату')
        verbose_name_plural = _('Заявки на оплату')
