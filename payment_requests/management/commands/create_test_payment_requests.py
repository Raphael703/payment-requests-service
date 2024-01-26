from django.core.management import BaseCommand
from tqdm import tqdm

from payment_requests.models import CheckingAccount
from payment_requests.tests.factories import PaymentRequestFactory


class Command(BaseCommand):
    help = 'Create test payment requests by existed checking accounts'

    def add_arguments(self, parser):
        parser.add_argument(
            'amount_of_checking_accounts',
            type=int,
            help='Amount of existed checking accounts'
        )
        parser.add_argument(
            'amount_of_payment_requests_for_each_checking_account',
            type=int,
            help='Amount of payment requests for each checking account'
        )

    def handle(self, *args, **kwargs):
        amount_of_checking_accounts = kwargs['amount_of_checking_accounts']
        amount_of_payment_requests_for_each_checking_account = kwargs[
            'amount_of_payment_requests_for_each_checking_account'
        ]

        all_checking_accounts = CheckingAccount.objects.all()[:amount_of_checking_accounts]
        for checking_account in tqdm(all_checking_accounts):
            for _ in range(amount_of_payment_requests_for_each_checking_account):
                PaymentRequestFactory(account=checking_account)

        total_payment_amount = (
                amount_of_checking_accounts * amount_of_payment_requests_for_each_checking_account
        )
        self.stdout.write(
            self.style.SUCCESS(f'Test payment requests created successfully. '
                               f'Amount - {total_payment_amount}')
        )
