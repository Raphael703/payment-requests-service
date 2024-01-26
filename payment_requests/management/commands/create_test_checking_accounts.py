from django.core.management import BaseCommand

from payment_requests.tests.factories import CheckingAccountFactory


class Command(BaseCommand):
    help = 'Create test checking accounts'
    AMOUNT_OF_OBJECTS = 50

    def handle(self, *args, **kwargs):
        for _ in range(self.AMOUNT_OF_OBJECTS):
            CheckingAccountFactory()
        self.stdout.write(
            self.style.SUCCESS(f'Test checking accounts created successfully. '
                               f'Amount - {self.AMOUNT_OF_OBJECTS}')
        )
