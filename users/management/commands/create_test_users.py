from django.core.management import BaseCommand

from users.tests.factories import UserFactory

import random


class Command(BaseCommand):
    help = 'Create test users'
    AMOUNT_OF_OBJECTS = 5
    DEFAULT_PASSWORD = 'qwer1234'

    def handle(self, *args, **kwargs):
        for _ in range(self.AMOUNT_OF_OBJECTS):
            is_staff = random.choice([True, False])
            user = UserFactory(is_staff=is_staff)
            user.set_password(self.DEFAULT_PASSWORD)
            user.save()

        self.stdout.write(
            self.style.SUCCESS(f'Test users created successfully. '
                               f'Amount - {self.AMOUNT_OF_OBJECTS},\n'
                               f'Default password: {self.DEFAULT_PASSWORD}')
        )
