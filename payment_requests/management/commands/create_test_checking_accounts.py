from django.core.management import BaseCommand
from tqdm import tqdm

from payment_requests.tests.factories import CheckingAccountFactory


class Command(BaseCommand):
    help = 'Create test checking accounts'

    def add_arguments(self, parser):
        parser.add_argument(
            'amount_of_objects',
            type=int,
            help='Amount object for create'
        )

    def handle(self, *args, **kwargs):
        amount_for_each_account = kwargs['amount_of_objects']
        for _ in tqdm(range(amount_for_each_account)):
            CheckingAccountFactory()
        self.stdout.write(
            self.style.SUCCESS(f'Test checking accounts created successfully. '
                               f'Amount - {amount_for_each_account}')
        )
