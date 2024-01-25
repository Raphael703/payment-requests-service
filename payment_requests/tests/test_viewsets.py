from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from payment_requests.tests.factories import PaymentRequestFactory


class InvoiceStatusAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.payment_request = PaymentRequestFactory()

    def test_get_invoice_status(self):
        url = reverse('get_invoice_status', args=[str(self.payment_request.id)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.payment_request.status)

    def test_get_invoice_status_not_found(self):
        invalid_uuid = str(self.payment_request.id)[:-5] + str(self.payment_request.id)[:5]
        url = reverse('get_invoice_status', args=[invalid_uuid])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('error', response.data)


class InvoiceCreateAPITestCase(APITestCase):

    def test_create_invoice(self):
        url = reverse('create_invoice', args=[0, 50.0])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('invoice_id', response.data)
        self.assertIn('account', response.data)

    def test_create_invoice_invalid_data(self):
        url = reverse('create_invoice', args=[0, 'invalid_amount'])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)
