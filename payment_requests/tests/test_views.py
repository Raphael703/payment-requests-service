from django.conf import settings
from django.test import TestCase
from django.urls import reverse

from payment_requests.models import CheckingAccount
from payment_requests.tests.factories import CheckingAccountFactory
from users.tests.tests import SetUpLoggedUserMixin


class TestPaymentRequestListView(SetUpLoggedUserMixin, TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.url = reverse('payment_requests_list')

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


class TestCheckingAccountFilerListView(SetUpLoggedUserMixin, TestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.url = reverse('checking_account_list')
        cls.checking_account = CheckingAccountFactory()

    def test_get_by_bare_user(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(list(response.context['checking_accounts']), CheckingAccount.objects.all())

    def test_get_by_staff_user(self):
        self.make_logged_user_staff()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_get_not_logged_in(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertRedirects(response, settings.LOGIN_URL)

    def test_filter_by_payment_type(self):
        filter_param = {'payment_type': self.checking_account.payment_type}
        response = self.client.get(self.url, filter_param)
        self.assertEqual(response.status_code, 200)

        self.assertQuerysetEqual(
            response.context['checking_accounts'],
            CheckingAccount.objects.filter(**filter_param)
        )

    def test_filter_by_card_type(self):
        filter_param = {'card_type': self.checking_account.card_type}
        response = self.client.get(self.url, filter_param)
        self.assertEqual(response.status_code, 200)

        self.assertQuerysetEqual(
            response.context['checking_accounts'],
            CheckingAccount.objects.filter(**filter_param)
        )

    def test_filter_by_account_type(self):
        filter_param = {'card_type': self.checking_account.account_type}
        response = self.client.get(self.url, filter_param)
        self.assertEqual(response.status_code, 200)

        self.assertQuerysetEqual(
            response.context['checking_accounts'],
            CheckingAccount.objects.filter(**filter_param)
        )

    def test_filter_by_owner_name(self):
        half_of_owner_name = self.checking_account.owner_name[
                             :len(self.checking_account.owner_name) // 2]
        filter_param = {
            'owner_name': half_of_owner_name
        }
        response = self.client.get(self.url, filter_param)
        self.assertEqual(response.status_code, 200)

        self.assertQuerysetEqual(
            response.context['checking_accounts'],
            CheckingAccount.objects.filter(owner_name__icontains=half_of_owner_name)
        )

    def test_filter_by_phone_number(self):
        half_of_phone_number = str(self.checking_account.phone_number)[
                               :len(self.checking_account.phone_number) // 2]
        filter_param = {
            'phone_number': half_of_phone_number
        }
        response = self.client.get(self.url, filter_param)
        self.assertEqual(response.status_code, 200)

        self.assertQuerysetEqual(
            response.context['checking_accounts'],
            CheckingAccount.objects.filter(phone_number__icontains=half_of_phone_number)
        )

    def test_filter_by_limit(self):
        half_of_limit = self.checking_account.limit // 2
        filter_param = {
            'limit_min': half_of_limit,
            'limit_max': self.checking_account.limit + half_of_limit
        }
        response = self.client.get(self.url, filter_param)
        self.assertEqual(response.status_code, 200)

        self.assertQuerysetEqual(
            response.context['checking_accounts'],
            CheckingAccount.objects.filter(
                limit__gte=half_of_limit, limit__lte=self.checking_account.limit)
        )
