from accounts import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _



def validate_positive(value):
    """Raise an error if user try to make a paymment or movement with amount value to 0

    Args:
        value (amount value): Amount value inserted by user in pay_form or movement_form

    Raises:
        ValidationError: [Message to the user for correction of the field value]
    """
    if value == 0:
        raise ValidationError(
            _('Please inster an amount value, it can not be 0'),
            params={'value': value},
        )

def validate_no_empty(value):

    if value == "empty":
        raise ValidationError(
            _('Bank name field can not be empty'),
            params={'value': value},
        )