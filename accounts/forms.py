from django import forms


class create_account_form(forms.Form):

    user = forms.CharField(max_length=100)
    account_name = forms.CharField(max_length=100) 
    account_value = forms.IntegerField()
    info = forms.Textarea()
    save_percent = forms.DecimalField(max_digits=4, decimal_places=2)
    saving_time = forms.IntegerField()
    date = forms.DateField()

class Pay_movement_form(forms.Form):

    account_id = forms.CharField(max_length=200)
    date = forms.DateField(null=True, blank=True, default=date.today)
    amount = forms.DecimalField(max_digits=11, decimal_places=2, help_text="Insert a negative number if you are paying")
    payee_payer = forms.CharField(max_length=50)
    EVENT_CHOICES = [
        ("card", "Card purchase"),
        # ("a_save", "Auto save"), We try using only save, if its necessary wee add this line for autosave like e-possu from nordea
        ("save", "Save"),
        ("o_transfer_out","Own transfer(Send out)"),
        ("o_transfer_in","Own transfer(Send in)"),
        ("payment", "Payment transfer"),
        ("deposit", "Deposit"),
    ]
    event = forms.CharField(max_length=14,choices=EVENT_CHOICES)
    message = forms.TextField(default="This is a default text", blank=True)
    account_value_before = forms.DecimalField(max_digits=11, decimal_places=2, help_text="leave empty, generated automatically", default=0)
    account_value_after = forms.DecimalField(max_digits=11, decimal_places=2,  help_text="leave empty, generated automatically", default=0)
