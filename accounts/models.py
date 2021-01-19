from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.dispatch import receiver
from django.db.models.signals import post_save
# from django.dispatch import receiver


class Account_value(models.Model):
    user = models.OneToOneField(User, 
                                    on_delete=models.CASCADE,#When user deleted profile should be deleted too
                                    null=False, blank=False)#This line tells that cant be a profile without a user 
    account_value = models.DecimalField(max_digits=11, decimal_places=2)

class Movements(models.Model):
    user = models.OneToOneField(User, 
                                    on_delete=models.CASCADE,#When user deleted profile should be deleted too
                                    null=False, blank=False)#This line tells that cant be a profile without a user 
    date = models.DateField(default=date.today)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    payee_payer = models.CharField(max_length=50)
    EVENT_CHOICES = [
        ("card", "Card purchase"),
        # ("a_save", "Auto save"), We try using only save, if its necessary wee add this line for autosave like e-possu from nordea
        ("save", "Save"),
        ("o_transfer","Own transfer"),
        ("payment", "Payment transfer"),
        ("deposit", "Deposit"),
    ]
    event = models.CharField(max_length=10,choices=EVENT_CHOICES)
    message = models.TextField(default="This is a default text", blank=True)

    def __str__(self):
        info = f"""{self.user.username}
            account value: {self.account_value}
            date:          {self.date}
            amount:        {self.amount}
            payee_payer:   {self.payee_payer}
            event:         {self.event}
            message:       {self.message}"""
        return info

@receiver(post_save, sender=Movements)#<---indicates that the function is a receiver of a signal: https://adriennedomingus.com/blog/signals-in-django
def update_account_value(sender, instance, **kwargs):
    Account_value.account_value = Account_value.account_value + Movements.amount
    instance.account_value.save()

# @receiver(post_save, sender=User)#<---indicates that the function is a receiver of a signal: https://adriennedomingus.com/blog/signals-in-django
# def save_profile_user(sender, instance, **kwargs):
#     instance.profile.save()