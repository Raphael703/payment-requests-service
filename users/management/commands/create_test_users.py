from django.core.management import BaseCommand
from tqdm import tqdm

from users.tests.factories import UserFactory

import random


class Command(BaseCommand):
    help = 'Create test users'
    DEFAULT_PASSWORD = 'qwer1234'

    def add_arguments(self, parser):
        parser.add_argument(
            'amount_of_objects',
            type=int,
            help='Amount of objects to create'
        )

    def handle(self, *args, **kwargs):
        amount_of_objects = kwargs['amount_of_objects']
        for _ in tqdm(range(amount_of_objects)):
            is_staff = random.choice([True, False])
            user = UserFactory(is_staff=is_staff)
            user.set_password(self.DEFAULT_PASSWORD)
            user.save()

        self.stdout.write(
            self.style.SUCCESS(f'Test users created successfully. '
                               f'Amount - {amount_of_objects},\n'
                               f'Default password: {self.DEFAULT_PASSWORD}')
        )
