import factory
from factory import fuzzy  # noqa

from payment_requests.consts import PAYMENT_REQUEST_STATUS, PAYMENT_TYPES, CARD_TYPES, CHECKING_ACCOUNT_TYPES
from payment_requests.models import PaymentRequest, CheckingAccount


class CheckingAccountFactory(factory.django.DjangoModelFactory):
    payment_type = factory.fuzzy.FuzzyChoice(
        p[0] for p in PAYMENT_TYPES)
    card_type = factory.fuzzy.FuzzyChoice(
        p[0] for p in CARD_TYPES)
    account_type = factory.fuzzy.FuzzyChoice(
        p[0] for p in CHECKING_ACCOUNT_TYPES)
    owner_name = factory.Faker('name')
    phone_number = factory.Faker(provider='phone_number', locale='ru')
    limit = factory.Faker(
        provider='pydecimal',
        left_digits=7, right_digits=2, positive=True
    )

    class Meta:
        model = CheckingAccount


class PaymentRequestFactory(factory.django.DjangoModelFactory):
    amount = factory.Faker(
        provider='pydecimal',
        left_digits=7, right_digits=2, positive=True
    )
    account = factory.SubFactory(CheckingAccountFactory)
    status = factory.fuzzy.FuzzyChoice(
        p[0] for p in PAYMENT_REQUEST_STATUS
    )

    class Meta:
        model = PaymentRequest
