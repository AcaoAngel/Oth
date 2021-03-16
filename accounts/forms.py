from django import forms
from datetime import date
from .models import Account_value, Movements
from .functions import validate_positive, validate_no_empty
from django.forms import ModelChoiceField
from django.contrib.auth.models import User



class Create_account_form(forms.ModelForm):

    
    account_name = forms.CharField(label='Account_name', required=True, max_length=100) 
    account_value = forms.IntegerField(label='Account value', required=True)
    info = forms.CharField(label="Content", widget=forms.Textarea)
    date = forms.DateField(label="Date", initial=date.today)

    class Meta():
        model = Account_value
        fields = ["date", 'account_name' , 'account_value', "info", ]

class Pay_form(forms.ModelForm):

    date = forms.DateField(label="Date", initial=date.today)
    amount = forms.DecimalField(label='Amount', required=True, max_digits=11, decimal_places=2, validators=[validate_positive])
    payee_payer = forms.CharField(label='Payer/Payee', max_length=100, required=False)
    EVENT_CHOICES = [
        ("empty",""),
        ("card", "Card purchase"),
        # ("a_save", "Auto save"), We try using only save, if its necessary wee add this line for autosave like e-possu from nordea
        ("payment", "Payment"),
        ("deposit", "Deposit"),
    ]
    event = forms.ChoiceField(label='Event', choices = EVENT_CHOICES, required=False)
    message = forms.CharField(label="Content", widget=forms.Textarea)
    # account_value_before = forms.DecimalField(label='Account value before', required=False)
    # account_value_after = forms.DecimalField(label='Account value after', required=False)

    class Meta():
        model = Movements
        fields = ['date' , 'amount' , 'payee_payer', 'event', 'message']

class Movement_form(forms.ModelForm):

    # account_id = forms.ModelChoiceField(label="From account", queryset=Movements.objects.filter(id=))
    date = forms.DateField(label="Date", initial=date.today)
    amount = forms.DecimalField(label='Amount', required=True, max_digits=11, decimal_places=2, validators=[validate_positive])#TODO validate positive is not needed anymore
    move_to_account = forms.ModelChoiceField(label="Moving to...", queryset=Account_value.objects.all())
    message = forms.CharField(label="Content", widget=forms.Textarea)
    # account_value_before = forms.DecimalField(label='Account value before', required=False)
    # account_value_after = forms.DecimalField(label='Account value after', required=False)




    class Meta():
        model = Movements
        fields = ['date' , 'amount', 'move_to_account', 'message']

    def __init__(self, current_account, *args, **kwargs):
        
        """Guide:
        https://simpleisbetterthancomplex.com/questions/2017/03/22/how-to-dynamically-filter-modelchoices-queryset-in-a-modelform.html
        Here in init we modificate the fields of the form using parameters got from the view, parameters are passed into this function
        and using fields[''].queryset we can modificate them on the time it is called from the view. 
        in the form use ModelChoiceField. It gives the whole name with id included, but that can be modified in the model class __str__
        """
        print(current_account.user_id)
        print(current_account.id)
        super(Movement_form, self).__init__(*args, **kwargs)
        self.fields["move_to_account"].queryset = Account_value.objects.filter(user_id=current_account.user_id).exclude(id=current_account.id)

        # previous way to list the accounts but was not effective and returnet all the accounts instead of only user accounts
        # def accounts_list_for_choices():
        #     account = models.Account_value.objects.all()
        #     choices = list()
        #     choices.append(("",""))
        #     inside_list = list()
        #     for i in account:
        #         inside_list = list(str(i.id))#as key we get the accoint id
        #         inside_list.append(i.account_name)
        #         choices.append(tuple(inside_list))
        #     print(choices)
        #     return choices


class UploadFileForm(forms.ModelForm):
    year = forms.IntegerField(validators=[validate_positive])
    BANK_CHOICES = [
        ("empty",""),
        ("nordea", "Nordea"),
        ("sp", "S-Pankki"),
    ]
    bank = forms.ChoiceField(label='Bank', choices = BANK_CHOICES, required=True, validators=[validate_no_empty])
    file = forms.FileField()

    class Meta():
        model = Movements
        fields = ["year", "bank", "file"]











