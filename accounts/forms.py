from django import forms
from datetime import date
from .models import Account_value, Movements


class Create_account_form(forms.Form):

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

class Pay_movement_form(forms.Form):

    account_id = forms.CharField(label='Account ID', required=True, max_length=100)
    date = forms.DateField(label="Date", initial=date.today)
    amount = forms.DecimalField(label='Amount', required=True)
    payee_payer = forms.CharField(label='Payer/Payee', required=True, max_length=100)
    # EVENT_CHOICES = [
    #     ("card", "Card purchase"),
    #     # ("a_save", "Auto save"), We try using only save, if its necessary wee add this line for autosave like e-possu from nordea
    #     ("save", "Save"),
    #     ("o_transfer_out","Own transfer(Send out)"),
    #     ("o_transfer_in","Own transfer(Send in)"),
    #     ("payment", "Payment transfer"),
    #     ("deposit", "Deposit"),
    # ]
    event = forms.CharField(label='Payer/Payee', required=True, max_length=100)
    message = forms.CharField(label="Content", widget=forms.Textarea)
    account_value_before = forms.DecimalField(label='Account value before', required=False)
    account_value_after = forms.DecimalField(label='Account value after', required=False)

    class Meta():
        model = Movements
        fields = ['account_id' , 'amount' , 'payee_payer']
