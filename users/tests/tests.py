from django.test import TestCase
from django.urls import reverse

from users.tests.factories import UserFactory

import faker


class SetUpLoggedUserMixin:
    @classmethod
    def setUpTestData(cls):
        cls.logged_user = UserFactory()
        cls.logged_user_password = faker.Faker().password()
        cls.logged_user.set_password(cls.logged_user_password)
        cls.logged_user.save()

    def setUp(self):
        self.client.login(username=self.logged_user.username,
                          password=self.logged_user_password)

    def make_logged_user_staff(self):
        self.logged_user.is_staff = True
        self.logged_user.save()


class TestUsersListView(SetUpLoggedUserMixin, TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.url = reverse('users_list')

    def test_get_by_bare_user(self):
        response = self.client.get(self.url)
        self.assertRedirects(response, reverse('index'))

    def test_get_by_staff_user(self):
        self.make_logged_user_staff()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_get_not_logged_in(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertRedirects(response, reverse('index'))
