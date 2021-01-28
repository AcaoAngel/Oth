from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.dispatch import receiver
from django.db.models.signals import post_save
# from django.dispatch import receiver


class Account_value(models.Model):
    user = models.ForeignKey(User, 
                                    on_delete=models.CASCADE,#When user deleted profile should be deleted too
                                    null=False, blank=False)#This line tells that cant be a profile without a user 
    account_name = models.CharField(max_length=100, default="Default account name")
    account_value = models.DecimalField(max_digits=11, decimal_places=2)
    info = models.TextField(max_length=500, default="Default info text")
    save_percent = models.DecimalField(max_digits=4, decimal_places=2, default=10)
    saving_time = models.IntegerField(help_text="Write here month amount for saving goal", default=12)
    date = models.DateField(null=True, blank=True, default=date.today)
    
    def __str__(self):
        return f"{self.user}: {self.account_name}: {self.account_value}"

class Movements(models.Model):
    # user = models.ForeignKey(User, 
    #                                 on_delete=models.CASCADE,#When user deleted profile should be deleted too
    #                                 null=False, blank=False)#This line tells that cant be a profile without a user 
    account_id = models.ForeignKey(Account_value,
                                    on_delete=models.CASCADE,#When user deleted profile should be deleted too
                                    null=False, blank=False, default=1)#This line tells that cant be a profile without a user
    date = models.DateField(null=True, blank=True, default=date.today)
    amount = models.DecimalField(max_digits=11, decimal_places=2, help_text="Insert a negative number if you are paying")
    payee_payer = models.CharField(max_length=50)
    EVENT_CHOICES = [
        ("card", "Card purchase"),
        # ("a_save", "Auto save"), We try using only save, if its necessary wee add this line for autosave like e-possu from nordea
        ("save", "Save"),
        ("o_transfer_out","Own transfer(Send out)"),
        ("o_transfer_in","Own transfer(Send in)"),
        ("payment", "Payment transfer"),
        ("deposit", "Deposit"),
    ]
    event = models.CharField(max_length=14,choices=EVENT_CHOICES)
    message = models.TextField(default="This is a default text", blank=True)
    account_value_before = models.DecimalField(max_digits=11, decimal_places=2, help_text="leave empty, generated automatically", default=0)
    account_value_after = models.DecimalField(max_digits=11, decimal_places=2,  help_text="leave empty, generated automatically", default=0)

    def __str__(self):
        return f"{self.account_id}: {self.date}: {self.amount}: {self.payee_payer}: {self.event}: "
  

@receiver(post_save, sender=Movements)#<-this decorator waits until new movement is created to aply account_value update
def update_account_value(sender, instance, **kwargs):# instance is the sender objet(Movement)
    """function for editing a table field after post from a different table
    in this function after adding a new movement is automatically sent the 
    signal for updating the account´s related account_value field calculating 
    the the current amount after paying or receiving money
    """
    
    editor = Account_value.objects.get(id=instance.account_id.id)#instance.this_table_field.foreign_key_field
    print(editor)
    instance.account_value_before = editor.account_value
    editor.account_value += instance.amount
    instance.account_value_after = editor.account_value
    editor.save()
    
    #hack to avoid save method from sending a signal. Without it we get recursive error 
    #EXPLANATION: If you look at the django model source code, specifically save_base(), 
    # you'll see that the pre_save() and post_save() signals are both wrapped in a conditional:
    # We can directly manipulate the meta options of a model or instance through
    # the _meta API which means we're able to 'disable' the signals from firing by setting 
    # auto_created = True on the instance we want to save.
    instance._meta.auto_created = True
    instance.save()
    instance._meta.auto_created = False
    



























# @receiver(post_save, sender=Movements)#<-this decorator waits until new movement is created to aply account_value update
# def update_account_value(sender, instance, **kwargs):
#     """function for creating a table field after post from a different table
#     in this function after adding a new movement is automatically sent the 
#     signal for creating the account´s new status field calculating 
#     the the current amount after paying or receiving money
#     """
#     pay = ["card", "o_transfer_out", "payment"]
#     if instance.EVENT_CHOICES in pay:
#         print("got in event choices")
#         if instance.amount > 0:
#             print("number greater the 0")
#             instance.amount = instance.amount *-1
#             print("converted number is", instance.amount)
#             instance.save()

#     user_object = Account_value.objects.get(user=instance.user.id)
#     print(user_object)

#     print(last_status)
#     new_value = last_status.account_value + instance.amount,
#     account_status = Account_value.objects.create(
#         user_id=Account_value.objects.get(user=instance.user.id, date=Movements.date.max()),
#         Account_value=new_value,
#         date = date.today()
#     )

