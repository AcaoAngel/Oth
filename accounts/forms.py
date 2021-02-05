from django import forms
from datetime import date
from .models import Account_value, Movements
from .functions import accounts_list_for_choices, validate_positive



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
    amount = forms.DecimalField(label='Amount', required=True, max_digits=11, decimal_places=2, 
                                validators=[validate_positive]
                                )
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
    amount = forms.DecimalField(label='Amount', required=True, max_digits=11, decimal_places=2, validators=[validate_positive])
    move_to_account = forms.ChoiceField(label="To account", choices = accounts_list_for_choices())
    message = forms.CharField(label="Content", widget=forms.Textarea)
    # account_value_before = forms.DecimalField(label='Account value before', required=False)
    # account_value_after = forms.DecimalField(label='Account value after', required=False)

    # def clean(self):
    #     cleaned_data = super().clean()
    #     account_id = cleaned_data.get("account_id")
    #     print("account_id",account_id)
    #     move_to_account = cleaned_data.get("move_to_account")
    #     print("move_to_account", move_to_account)

    #     if not account_id:
    #         print("there is not an account id")
    #     if account_id and move_to_account:
    #         if account_id == move_to_account:
    #             print("raising the error")
    #             raise forms.ValidationError("You can not move money to the same account")



    class Meta():
        model = Movements
        fields = ['date' , 'amount', 'move_to_account', 'message']