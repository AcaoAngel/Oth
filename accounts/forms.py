from django import forms
from datetime import date
from .models import Account_value, Movements
from .functions import accounts_list_for_choices


class Create_account_form(forms.ModelForm):

    user = forms.CharField(label='User', required=True, max_length=100)
    account_name = forms.CharField(label='Account_name', required=True, max_length=100) 
    account_value = forms.IntegerField(label='Account value', required=True)
    info = forms.CharField(label="Content", widget=forms.Textarea)
    save_percent = forms.DecimalField(label='Save percent', required=True)
    saving_time = forms.IntegerField(label='Saving time', required=True)
    date = forms.DateField(label="Date", initial=date.today)

    class Meta():
        model = Account_value
        fields = ['user' , 'account_name' , 'account_value']

class Pay_form(forms.ModelForm):

    date = forms.DateField(label="Date", initial=date.today)
    amount = forms.DecimalField(label='Amount', required=True)
    payee_payer = forms.CharField(label='Payer/Payee', max_length=100, required=False)
    EVENT_CHOICES = [
        ("empty",""),
        ("card", "Card purchase"),
        # ("a_save", "Auto save"), We try using only save, if its necessary wee add this line for autosave like e-possu from nordea
        ("save", "Save"),
        ("o_transfer_out","Own transfer(Send out)"),
        ("o_transfer_in","Own transfer(Send in)"),
        ("payment", "Payment transfer"),
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

    date = forms.DateField(label="Date", initial=date.today)
    amount = forms.DecimalField(label='Amount', required=True)
    move_to_account = forms.ChoiceField(choices = accounts_list_for_choices())
    message = forms.CharField(label="Content", widget=forms.Textarea)
    # account_value_before = forms.DecimalField(label='Account value before', required=False)
    # account_value_after = forms.DecimalField(label='Account value after', required=False)

    class Meta():
        model = Movements
        fields = ['date' , 'amount', 'move_to_account', 'message']