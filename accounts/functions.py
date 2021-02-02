from .models import Account_value

def accounts_list_for_choices():
    account = Account_value.objects.all()
    choices = list()
    choices.append(("empty_field",""))
    inside_list = list()
    for i in account:
        inside_list = list(str(i.id))#as key we get the accoint id
        inside_list.append(i.account_name+str(i.account_value))
        choices.append(tuple(inside_list))
        print(choices)
    return choices