from accounts import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _







def validate_positive(value):
    if value < 0:
        raise ValidationError(
            _('Amount must be a positive number'),
            params={'value': value},
        )

def validate_not_same_account(value, id):
    def innerfn(value):
        if value == id:
            raise ValidationError(
                _('You can not send to same account'),
                params={'value': value},
            )