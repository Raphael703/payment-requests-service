from _decimal import Decimal

from django.utils.translation import gettext_lazy as _
from model_utils import Choices

PAYMENT_REQUEST_STATUS = Choices(
    (0, 'AWAITING', _('Ожидает оплаты')),
    (1, 'PAID', _('Оплачена')),
    (2, 'CANCELLED', _('Отменена'))
)

PAYMENT_TYPES = Choices(
    (0, 'CARD', _('Карта')),
    (1, 'CHECKING_ACCOUNT', _('Платежный счет'))
)

CARD_TYPES = Choices(
    (0, 'DEBIT', _('DEBIT')),
    (1, 'CREDIT', _('CREDIT')),
    (2, 'PREPAID', _('PREPAID')),
    (3, 'SAVINGS', _('SAVINGS')),
    (4, 'PLATINUM', _('PLATINUM')),
    (5, 'TRAVEL', _('TRAVEL')),
    (6, 'LOYALTY', _('LOYALTY'))
)

CHECKING_ACCOUNT_TYPES = Choices(
    (0, 'CURRENT', _('Текущий (чековый)')),
    (1, 'SAVINGS', _('Сберегательный')),
    (4, 'BUSINESS', _('Бизнес')),
    (5, 'PAYROLL', _('Зарплатный')),
    (6, 'STUDENT', _('Студенческий')),
    (7, 'JOINT', _('Совместный')),
    (8, 'HIGH_INTEREST', _('С высокой процентной ставкой'))
)

DEFAULT_CHECKING_ACCOUNT_LIMIT = Decimal(1000.00)
