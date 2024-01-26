from django.contrib import admin

from payment_requests.models import CheckingAccount, PaymentRequest


@admin.register(CheckingAccount)
class CheckingAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment_type', 'card_type', 'account_type',
                    'owner_name', 'phone_number', 'limit', 'created_at',
                    'updated_at')
    search_fields = ('id', 'owner_name', 'phone_number')
    list_filter = ('payment_type', 'card_type', 'account_type')


@admin.register(PaymentRequest)
class PaymentRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'account', 'status', 'created_at', 'updated_at')
    search_fields = ('id', 'amount')
    list_filter = ('status',)
