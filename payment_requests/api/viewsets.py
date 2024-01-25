from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from payment_requests.api.serializers import PaymentRequestSerializer, CheckingAccountSerializer
from payment_requests.api.swagger_responses_examples import responses_schema_for_create_invoice, \
    responses_schema_for_get_invoice_status
from payment_requests.models import PaymentRequest


class InvoiceStatusAPIView(APIView):

    @swagger_auto_schema(
        operation_description='Return invoice status by invoice id (uuid)',
        responses=responses_schema_for_get_invoice_status
    )
    def get(self, request, invoice_id):
        try:
            payment_request = PaymentRequest.objects.get(id=invoice_id)
            serializer = PaymentRequestSerializer(payment_request)
            return Response(serializer.data['status'])
        except PaymentRequest.DoesNotExist:
            return Response({'error': 'Payment request not found'},
                            status=status.HTTP_404_NOT_FOUND)


class InvoiceCreateAPIView(APIView):

    @swagger_auto_schema(
        operation_description='Create a new invoice by {payment_type}(of checking account) '
                              'and {amount} of invoice(payment_request)',
        responses=responses_schema_for_create_invoice,
    )
    def post(self, request, payment_type, amount):
        try:
            checking_account_data = {'payment_type': payment_type}
            checking_account_serializer = CheckingAccountSerializer(data=checking_account_data)
            checking_account_serializer.is_valid(raise_exception=True)
            checking_account = checking_account_serializer.save()

            payment_request_data = {
                'amount': amount,
                'account': checking_account,
            }
            payment_request = PaymentRequest.objects.create(**payment_request_data)

            return Response(
                {'invoice_id': str(payment_request.id),
                 'account': checking_account_serializer.data},
                status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
