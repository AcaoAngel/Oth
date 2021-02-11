from django.contrib.auth.models import User
from .models import Movements, Account_value
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete, post_init

# presave_move_to_account = int()
# @receiver(post_init, sender=Movements)# this decorator gives me the info before saving
# def save_to_global(sender, instance, **kwargs):# instance is the sender objet(Movement)
#     print("getting in post_init")
#     global presave_move_to_account 
#     presave_move_to_account = instance.move_to_account
#     print(presave_move_to_account)

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
            instance.move_to_account_prestate = True #To know was a movement o not before save we use this function and update it here
            save_without_signal(instance)
    else: #For editing case
        account_value_tmp = update_current_movement(instance, created)
        update_recursively_movements(instance, account_value_tmp)
        

@receiver(post_delete, sender=Movements)
def undo_payment(sender, instance, **kwargs):
    print("getting in post delete receiver")
    editor = Account_value.objects.get(id=instance.account_id.id)# ACCOUNT moving the money object
    editor.account_value -= instance.amount#Calculate the new account value
    
    try:#Here we create automatically the movement in the second account if we are moving money.
        #If we get and error at creating the second account movement the first movement is gonna be created anyway, 
        #Because of that when deleting that first movement we need to catch the error of second account movement not found
        update_recursively_movements(instance, account_value_tmp=instance.account_value_before)
        if instance.move_to_account:#Here if we are moving we update the second account. HINT: Move to account is saved as string
            movement_in_second_account(instance)
            print("second account id is: ",instance)
            linked_movement = Movements.objects.get(id = instance.second_account_movement_id)
            delete_without_signal(linked_movement)
    except:
        pass

    editor.save()


#-----------Functions for signals------------------------

def update_current_movement(instance, created):
    #Update the amount, account_value_before and account_value_after

    # instance = Movements.objects.get(id=instance.id)#get the object of the current movement
    editor = Account_value.objects.get(id=instance.account_id.id)#the second account
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


def update_recursively_movements(instance, account_value_tmp):#Instance is the actual movement
    """This function update in the rest of account movements the account_value_before and account_value_after variables 
    for the account paying and the account receiving if it is the case. 
    
    OTHER OPTION NOT WORKING WELL: In this case is not possible to only set if i.date > instance.date becouse when added movements
    from the admin the time can be exactly the same for some movements when we use 'save and add another' options
    so works better to allways skip the current edited movement.

    Args:
        instance (Django query object): [Takes the object of the current movement]
        account_value_tmp (int): the account_value_bejore or after depending of 
        the accion, for editing its passed the account_value_after, for deleting its needed the account_value_before
    """
    account_movements = Movements.objects.filter(account_id = instance.account_id.id)#get all the movements of the instanciated account(account moving)

    # account_value_tmp = int()
    for i in account_movements:#Update the movements for the rest of movements in the moving account
        if i.id > instance.id:#skip all the previous movements including the actual
            print("editting", i)
            i.account_value_before = account_value_tmp
            i.account_value_after = account_value_tmp + i.amount
            account_value_tmp = i.account_value_after
            save_without_signal(i)
        
    if instance.move_to_account:#Update the rest of the movements in the second account
        account_value_tmp = Movements.objects.get(id = instance.second_account_movement_id).account_value_after
        print("got in instance.move_to_acco1unt")
        print("account value temp is:", account_value_tmp)
        second_account_movements = Movements.objects.filter(account_id = instance.move_to_account)#get all the movements of the instanciated account(second account)
        print(second_account_movements)
        for i in second_account_movements:
            print("i id id:", i.id)
            print("instance second account movement id is:", instance.second_account_movement_id)
            if i.id > instance.second_account_movement_id:#skip all the previous movements including the actual of the second account
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

def delete_without_signal(instance):
    instance._meta.auto_created = True
    instance.delete()
    instance._meta.auto_created = False



def movement_in_second_account(instance, created=None, previous_amount=0):
    """Here if we are moving we update the second account. HINT: Move to account is saved as string

    Args:
        instance (Queryset object): [is the object of the movement the user is operating with]
        created ([Boolean], optional): [description]. Defaults to None to implement delete statement.
        previous_amount ([Int], optional): [description]. Defaults to 0. This is a necessary variable for editing 
    """
    account_receiving = Account_value.objects.get(id = instance.move_to_account)
    if created:#For creating
        print("getting in movement_in_second_account created")
        account_receiving.account_value -= instance.amount
        
    elif created == False:#For editing
        if instance.move_to_account_prestate:
            print("updating when there was allready a movement")
            print("previous amount ", previous_amount)
            print("instance amount ", instance.amount)
            account_receiving.account_value += previous_amount#Undo the previos movement in the account
            account_receiving.account_value -= instance.amount#Calculate the new account value
        else:
            print("Update when there was not a movement")
            account_receiving.account_value -= instance.amount#update the second own account
    else:#For deleting
        print("getting in movement_in_second_account deleted")
        account_receiving.account_value += instance.amount#Undo the previos movement in the account
    second_account_movement(instance, created, account_receiving)
    account_receiving.save()
    


def second_account_movement(instance, created, account_receiving):#Instance: movement moving the money. account_receiving: the money receiver account
    #Here we create, edit only the movement done in the second account, re rest of movements are updated in the update_recursively_movements function
    # instance = Movements.objects.get(id=instance.id)#the account moving the money
    # account_receiving = Account_value.objects.get(id=instance.move_to_account)#the account receiving the money
    def create(instance, account_receiving):
        movement_info = Movements()
        movement_info.account_id = account_receiving
        movement_info.date = instance.date
        movement_info.amount = instance.amount * -1
        movement_info.moved_from_account = instance.account_id.id
        movement_info.message = instance.message
        movement_info.account_value_before = account_receiving.account_value + instance.amount #we use plus because instance.amount is a negative number
        print(account_receiving.account_value,"....", instance.amount)
        movement_info.account_value_after = account_receiving.account_value
        movement_info.move_to_account_prestate = True
        print("movement info id is: " ,movement_info.id, type(movement_info.id))
        movement_info.second_account_movement_id = instance.id
        save_without_signal(movement_info)
        instance.second_account_movement_id = movement_info.id#Update the field  in the instance after create the second account movement.
        #We dont need to save it here becouse is saved in future step. If we do it here we create it twice
    if created:
        create(instance, account_receiving)
    elif created == False:
        if instance.move_to_account_prestate:#We update here the date, amount and message. 
            #If idea is to send the money to another account user have to delete and create a new movement
            update_the_second_account = Movements.objects.get(id=instance.second_account_movement_id)
            update_the_second_account.date = instance.date
            update_the_second_account.amount = instance.amount * -1
            update_the_second_account.message = instance.message
            update_the_second_account.account_value_after = update_the_second_account.account_value_before + update_the_second_account.amount
            save_without_signal(update_the_second_account)
        else:#user cant edit a payment to make it a movement, this option is only allowed from admin panel
            create(instance, account_receiving)
    else:#for deleting, done directly in the post_delete signal.
        pass






