from drf_yasg import openapi

from payment_requests.consts import PAYMENT_REQUEST_STATUS

responses_schema_for_create_invoice = {
    200: openapi.Response(
        description='Created - Successfully created the invoice',
        examples={
            'application/json': {
                'invoice_id': 'abaf4433-c73a-4ee2-8b19-8eb95cee76ef',
                'account': {
                    'id': '4d02c251-3ea4-4376-a5b0-5ed89135169d',
                    'payment_type': 1,
                    'card_type': 0,
                    'account_type': 0,
                    'owner_name': 'null',
                    'phone_number': 'null',
                    'limit': '1000.00'
                }
            }
        }
    ),
    400: 'Bad Request - Invalid input data',
}

responses_schema_for_get_invoice_status = {
    200: f'Returning a status of invoice(positive int), \n'
         f'statuses schema: {PAYMENT_REQUEST_STATUS}',
    400: 'Bad Request - Invalid input data or invoice does not exist',
}
