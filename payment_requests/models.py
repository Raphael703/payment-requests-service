import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from payment_requests.consts import PAYMENT_REQUEST_STATUS, PAYMENT_TYPES, \
    CARD_TYPES, CHECKING_ACCOUNT_TYPES, DEFAULT_CHECKING_ACCOUNT_LIMIT
from payment_requests.utils import format_name


class CheckingAccount(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payment_type = models.PositiveSmallIntegerField(
        verbose_name=_('Тип платежа'),
        choices=PAYMENT_TYPES, default=PAYMENT_TYPES.CARD,
        db_index=True
    )
    card_type = models.PositiveSmallIntegerField(
        verbose_name=_('Тип карты'),
        choices=CARD_TYPES, default=CARD_TYPES.DEBIT,
        db_index=True
    )
    account_type = models.PositiveSmallIntegerField(
        verbose_name=_('Тип счёта'),
        choices=CHECKING_ACCOUNT_TYPES, default=CHECKING_ACCOUNT_TYPES.CURRENT,
        db_index=True
    )
    owner_name = models.CharField(
        verbose_name=_('ФИО владельца'),
        max_length=255,
        db_index=True,
        blank=True, null=True
    )
    phone_number = PhoneNumberField(
        verbose_name=_('Номер телефона'),
        db_index=True,
        blank=True, null=True
    )
    limit = models.DecimalField(
        verbose_name=_('Лимит'),
        max_digits=10, decimal_places=2,
        default=DEFAULT_CHECKING_ACCOUNT_LIMIT,
        db_index=True
    )
    created_at = models.DateTimeField(
        verbose_name=_('Дата и время создания'),
        editable=False, auto_now_add=True, db_index=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_('Дата и время обновления'),
        editable=False, auto_now=True, db_index=True,
    )

    def __str__(self):
        return (f'{format_name(self.owner_name)} / '
                f'{self.get_payment_type_display()}')

    class Meta:
        verbose_name = _('Реквизит')
        verbose_name_plural = _('Реквизиты')
        ordering = ['-created_at']


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
        choices=PAYMENT_REQUEST_STATUS,
        default=PAYMENT_REQUEST_STATUS.AWAITING
    )
    created_at = models.DateTimeField(
        verbose_name=_('Дата и время создания'),
        editable=False, auto_now_add=True, db_index=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_('Дата и время обновления'),
        editable=False, auto_now=True, db_index=True,
    )

    def __str__(self):
        return f'Заявка # {self.id} - Сумма: {self.amount}'

    class Meta:
        verbose_name = _('Заявка на оплату')
        verbose_name_plural = _('Заявки на оплату')
        ordering = ['-created_at']
