from accounts import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _



def validate_positive(value):
    if value == 0:
        raise ValidationError(
            _('Please inster an amount value, it can not be 0'),
            params={'value': value},
        )
