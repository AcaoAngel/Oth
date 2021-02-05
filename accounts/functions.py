from accounts import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _



def accounts_list_for_choices():
    account = models.Account_value.objects.all()
    choices = list()
    choices.append(("",""))
    inside_list = list()
    for i in account:
        inside_list = list(str(i.id))#as key we get the accoint id
        inside_list.append(i.account_name)
        choices.append(tuple(inside_list))
    print(choices)
    return choices



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