from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Account_value(models.Model):
    user = models.ForeignKey(User, 
                                    on_delete=models.CASCADE,#When user deleted profile should be deleted too
                                    null=False, blank=False)#This line tells that cant be a profile without a user 
    account_name = models.CharField(max_length=100, default="Default account name")
    account_value = models.DecimalField(max_digits=11, decimal_places=2)
    info = models.TextField(max_length=500, default="Default info text")
    save_percent = models.DecimalField(max_digits=4, decimal_places=2, default=10)
    saving_time = models.IntegerField(help_text="Write here month amount for saving goal", default=12)
    date = models.DateTimeField(null=True, blank=True, default=timezone.now())

    def get_absolute_url(self):
        return 
    
    def __str__(self):
        return f"{self.id}: {self.user}: {self.account_name}: {self.account_value}"

class Movements(models.Model):
    # user = models.ForeignKey(User, 
    #                                 on_delete=models.CASCADE,#When user deleted profile should be deleted too
    #                                 null=False, blank=False)#This line tells that cant be a profile without a user 
    account_id = models.ForeignKey(Account_value,
                                    on_delete=models.CASCADE,#When user deleted profile should be deleted too
                                    null=False, blank=False)#This line tells that cant be a profile without a user
    date = models.DateTimeField(null=True, blank=True, default=timezone.now())
    amount = models.DecimalField(max_digits=11, decimal_places=2, help_text="Insert a negative number if you are paying", default=10)
    payee_payer = models.CharField(max_length=50, default="default payer")
    EVENT_CHOICES = [
        ("card", "Card purchase"),
        # ("a_save", "Auto save"), We try using only save, if its necessary wee add this line for autosave like e-possu from nordea
        ("save", "Save"),
        ("o_transfer_out","Own transfer(Send out)"),
        ("o_transfer_in","Own transfer(Send in)"),
        ("payment", "Payment transfer"),
        ("deposit", "Deposit"),
    ]
    event = models.CharField(max_length=14,choices=EVENT_CHOICES, default="card")
    message = models.TextField(default="This is a default text", blank=True)
    account_value_before = models.DecimalField(max_digits=11, decimal_places=2, help_text="leave empty, generated automatically", default=0)
    account_value_after = models.DecimalField(max_digits=11, decimal_places=2,  help_text="leave empty, generated automatically", default=0)


    def __str__(self):
        return f"""{self.id}: {self.date}: {self.account_id.user}: {self.amount}: {self.payee_payer}: {self.event}: {self.account_value_after}"""
  


    




















