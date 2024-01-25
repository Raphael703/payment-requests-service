from rest_framework import serializers

from payment_requests.models import PaymentRequest, CheckingAccount


class PaymentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentRequest
        fields = '__all__'


class CheckingAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckingAccount
        fields = '__all__'
