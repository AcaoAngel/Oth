from django.contrib.auth.models import User
from .models import Movements, Account_value
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete, post_init

presave_move_to_account = int()

@receiver(post_init, sender=Movements)# this decorator gives me the info before saving
def save_to_global(sender, instance, **kwargs):# instance is the sender objet(Movement)
    print("getting in post_init")
    global presave_move_to_account 
    presave_move_to_account = instance.move_to_account
    print(presave_move_to_account)

@receiver(post_save, sender=Movements)#<-this decorator waits until new movement is created to aply account_value update
def payment(sender, instance, created, **kwargs):# instance is the sender objet(Movement)
    """function for editing a table field after post from a different table
    in this function after adding a new movement is automatically sent the 
    signal for updating the account´s related account_value field calculating 
    the the current amount after paying or receiving money
    """
    if created:
        editor = Account_value.objects.get(id=instance.account_id.id)#instance.this_table_field.foreign_key_field
        instance.account_value_before = editor.account_value
        editor.account_value += instance.amount
        instance.account_value_after = editor.account_value
        editor.save()
        save_without_signal(instance)
        if instance.move_to_account:#Here if we are moving we update the second account. HINT: Move to account is saved as string
            movement_in_second_account(instance, created)
    else: #For editing case
        account_value_tmp = update_current_movement(instance, created)
        update_recursively_movements(instance, account_value_tmp)
        

@receiver(post_delete, sender=Movements)
def undo_payment(sender, instance, **kwargs):
    editor = Account_value.objects.get(id=instance.account_id.id)
    # editor.account_value = instance.account_value_before#bring back the previous account value
    editor.account_value -= instance.amount#Calculate the new account value
    # instance.account_value_after = editor.account_value#Save the new account value in the movement for references
    editor.save()
    print(instance.account_value_after)
    update_recursively_movements(instance, account_value_tmp=instance.account_value_before)
    if instance.move_to_account:#Here if we are moving we update the second account. HINT: Move to account is saved as string
        movement_in_second_account(instance)


#-----------Functions for signals------------------------

def update_current_movement(instance, created):
    current_movement = Movements.objects.get(id=instance.id)#get the object of the current movement
    editor = Account_value.objects.get(id=instance.account_id.id)#get the object of the linked account
    previous_amount = instance.account_value_after - instance.account_value_before#before changing the account_value_before and after we get the previous amount
    editor.account_value -= previous_amount#Undo the previos movement in the account
    editor.account_value += instance.amount#Calculate the new account value if there was a movement
    if instance.move_to_account:#Here if we are moving we update the second account. HINT: Move to account is saved as string
        movement_in_second_account(instance, created, previous_amount)#Update the new amount in the moved to account
    instance.account_value_after = instance.account_value_before + instance.amount#Save the new account value in the movement for references
    account_value_tmp = instance.account_value_after
    editor.save()
    save_without_signal(instance)
    return account_value_tmp


def update_recursively_movements(instance, account_value_tmp):#in instance function takes the user
    """In this case is not possible to only set if i.date > instance.date becouse when added movements
    from the admin the time can be exactly the same for some movements when we use 'save and add another' options
    so works better to allways skip the current edited movement

    Args:
        instance (Django query object): [Takes the object of the current movement]
        account_value_tmp (int): the account_value_bejore or after depending of 
        the accion, for editing its passed the account_value_after, for deleting its needed the account_value_before
    """
    user_movements = Movements.objects.filter(account_id = instance.account_id.id)#get all the movements of the instanciated user

    # account_value_tmp = int()
    for i in user_movements:
        if i.id > instance.id:#skip all the previous movements including the actual
            print("editting", i)
            i.account_value_before = account_value_tmp
            i.account_value_after = account_value_tmp + i.amount
            account_value_tmp = i.account_value_after
            save_without_signal(i)
 


def save_without_signal(instance):
    """Hack to avoid save method from sending a signalcreating a recursive error 
        EXPLANATION: 
        If you look at the django model source code, specifically save_base(), 
        you'll see that the pre_save() and post_save() signals are both wrapped in a conditional:
        We can directly manipulate the meta options of a model or instance through
        the _meta API which means we're able to 'disable' the signals from firing by setting 
        auto_created = True on the instance we want to save.
    """
    instance._meta.auto_created = True
    instance.save()
    instance._meta.auto_created = False



def movement_in_second_account(instance, created=None, previous_amount=0):
    """Here if we are moving we update the second account. HINT: Move to account is saved as string

    Args:
        instance (Queryset object): [is the object of the movement the user is operating with]
        created ([Boolean], optional): [description]. Defaults to None to implement delete statement.
        previous_amount ([Int], optional): [description]. Defaults to 0. This is a necessary variable for editing 
    """
    




    print(id, type(id))
    moved_to = Account_value.objects.get(id = instance.move_to_account)
    if created:#For creating
        print("getting in movement_in_second_account created")
        moved_to.account_value += instance.amount
    elif created == False:#For editing
        if presave_move_to_account:
            print("updating when there was allready a movement")
            moved_to.account_value -= previous_amount#Undo the previos movement in the account
            moved_to.account_value += instance.amount#Calculate the new account value
        else:
            print("Update when there was not a movement")
            moved_to.account_value -= previous_amount#update the second own account
        print("getting in movement_in_second_account edited")
        print(previous_amount)
        moved_to.account_value -= previous_amount#Undo the previos movement in the account
        moved_to.account_value += instance.amount#Calculate the new account value
    else:#For deleting
        print("getting in movement_in_second_account deleted")
        moved_to.account_value -= previous_amount#Undo the previos movement in the account
    moved_to.save()

























# def create_movement_in_second_account(instance):
#     """Here if we are moving we update the second account. HINT: Move to account is saved as string

#     Args:
#         instance ([Queryset object]): [is the object of the movement the user is operating with]
#     """
    
#     moved_to = Account_value.objects.get(id = int(id))
#     moved_to.account_value += instance.amount
#     moved_to.save()


# def edit_movement_in_second_account(instance, previous_amount):
#     """Here if we are moving we update the second account. HINT: Move to account is saved as string

#     Args:
#         instance ([Queryset object]): [is the object of the movement the user is operating with]
#     """
    
#     moved_to = Account_value.objects.get(id = int(id))
#     editor.account_value -= previous_amount#Undo the previos movement in the account
#     editor.account_value += instance.amount#Calculate the new account value
#     moved_to.save()

# def delete_movement_in_second_account(instance):
#     moved_to = Account_value.objects.get(id = int(id))
#     editor.account_value -= previous_amount#Undo the previos movement in the account
#     moved_to.save()