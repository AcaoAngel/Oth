from django.db import models
from django.contrib.auth.models import User
from datetime import date
import accounts.functions





class Account_value(models.Model):
    user = models.ForeignKey(User, 
                                    on_delete=models.CASCADE,#When user deleted account should be deleted too
                                    null=False, blank=False)#This line tells that cant be an account without a user 
    account_name = models.CharField(max_length=100, default="")
    account_value = models.DecimalField(max_digits=11, decimal_places=2)
    info = models.TextField(max_length=500, default="Default info text")
    save_percent = models.DecimalField(max_digits=4, decimal_places=2, default=10)
    saving_time = models.IntegerField(help_text="Write here month amount for saving goal", default=12)
    date = models.DateField(null=True, blank=True, default=date.today())

    def get_absolute_url(self):
        return 
    
    def __str__(self):
        return f"{self.account_name}: {self.account_value}"

class Movements(models.Model):
    account_id = models.ForeignKey(Account_value,
                                    on_delete=models.CASCADE,#When account deleted movements should be deleted too
                                    null=False, blank=False)#This line tells that cant be a movement without an account
    date = models.DateField(null=True, blank=True, default=date.today())
    amount = models.DecimalField(max_digits=11, decimal_places=2, help_text="Insert a negative number if you are paying")
    move_to_account = models.CharField(max_length=100, blank=True, null=True, default= None)
    payee_payer = models.CharField(max_length=50, default="default payer", blank=True, null=True)
    event = models.CharField(max_length=14, blank=True, null=True)
    message = models.TextField(default="This is a default text", blank=True)
    account_value_before = models.DecimalField(max_digits=11, decimal_places=2, help_text="leave empty, generated automatically", default=0)
    account_value_after = models.DecimalField(max_digits=11, decimal_places=2,  help_text="leave empty, generated automatically", default=0)
    move_to_account_prestate = models.BooleanField(max_length=100, default=False)


    def __str__(self):
        return f"""{self.id}: {self.date}: {self.account_id.user}: {self.amount}: {self.payee_payer}: {self.event}: {self.account_value_after}"""


    
    
    
  



    




















