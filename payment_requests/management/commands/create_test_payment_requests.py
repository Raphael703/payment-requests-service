from django.core.management import BaseCommand

from payment_requests.models import CheckingAccount
from payment_requests.tests.factories import PaymentRequestFactory


class Command(BaseCommand):
    help = 'Create test payment requests by existed checking accounts'
    AMOUNT_OF_OBJECTS_FOR_EACH_ACCOUNT = 50

    def handle(self, *args, **kwargs):
        all_checking_accounts = CheckingAccount.objects.all()
        for checking_account in all_checking_accounts:
            for _ in range(self.AMOUNT_OF_OBJECTS_FOR_EACH_ACCOUNT):
                PaymentRequestFactory(account=checking_account)
        total_payment_amount = (
            all_checking_accounts.count() * self.AMOUNT_OF_OBJECTS_FOR_EACH_ACCOUNT
        )
        self.stdout.write(
            self.style.SUCCESS(f'Test payment requests created successfully. '
                               f'Amount - {total_payment_amount}')
        )
