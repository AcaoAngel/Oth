from django.shortcuts import render, get_object_or_404, redirect
from .forms import Create_account_form, Pay_form, Movement_form, UploadFileForm
from .models import Account_value, Movements
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.models import User
from decimal import Decimal
import accounts.read_tiliote
from django.core.paginator import Paginator



# class view_accounts(ListView):
    
#     def get_queryset(self):
#         if self.request.user.is_authenticated:
#             paginate_by = 4
#             self.template_name = "view_accounts.html"

#             current_user_account = Account_value.objects.filter(user_id=self.request.user.id)

#             return current_user_account
            
#         self.template_name = "access_denied_accounts.html"

def view_accounts(request):
    current_user_account = Account_value.objects.filter(user_id=request.user.id)
    paginator = Paginator(current_user_account, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    

    return render(request, "view_accounts.html", {"object_list": current_user_account, "page_obj": page_obj })

def account_detail(request, id):
    # print("loading from account detail")
   
    account = Account_value.objects.get(id=id)
    # print(type(account.id), account.id)
    request.session["account_id"] = id 

    movements = Movements.objects.filter(account_id_id=id)
    paginator = Paginator(movements, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'account':account, 'movements':page_obj}
        
    return render(request, "account_detail.html", context)

def sure_delete(request, id, movement_id):
    print("loading form sure delete")
    account = Account_value.objects.get(id=id)
    print(type(account.id), account.id)
    request.session["account_id"] = id 
    movements = Movements.objects.filter(account_id_id=id)
    deleting_movement = Movements.objects.get(id=movement_id)
    if request.method == "POST":
        
        print("post done succesfully")
        to_delete = Movements.objects.get(id = movement_id)
        to_delete.delete()
        return redirect("/transaction_done/")

    movements = Movements.objects.filter(account_id_id=id)
    paginator = Paginator(movements, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'account':account, 'movements':page_obj, 'sure_delete':True, "deleting_movement":deleting_movement}

    return render(request, "account_detail.html", context)

def delete_account(request, id):
    account = Account_value.objects.get(id=id)
    if request.method == "POST":
        
        print("post done succesfully")
        account.delete()
        return redirect("/account_deleted/")

    movements = Movements.objects.filter(account_id_id=id)
    paginator = Paginator(movements, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'account':account, 'delete_account':True, 'movements':page_obj}

    return render(request, "account_detail.html", context)

def create_account(request):
    if request.method == "POST":
        form = Create_account_form(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = User.objects.get(id = request.user.id)#Account_value.objects.get(id=request.session["account_id"])
            form.account_name = request.POST["account_name"]
            form.account_value = request.POST["account_value"]
            form.info = request.POST["info"]
            form.date = request.POST["date"]
            form.save()
            return redirect("/account_created/")

        else:
            return render(request, "account_value_form.html", {"form":form})
            print("form is not valid")
    
    form = Create_account_form()
    return render(request, "account_value_form.html", {"form":form})

def movements_form(request):#account id is sended using the parameter through url

    current_account = get_object_or_404(Account_value, id = request.session["account_id"])

    # if request.method=="GET":
    #     current_account_id = get_object_or_404(Account_value, id = request.session["account_id"])
    #     print("got in GET",current_account_id)
        

    if request.method=="POST":
        print("post done")

        # form=Movement_form(request.POST, user = request.user, account_id = request.session["account_id"])
        form=Movement_form(current_account, request.POST)

        if form.is_valid():
            print("form is valid")

            form = form.save(commit = False)
            form.account_id = Account_value.objects.get(id = request.session["account_id"])#Account_value.objects.get(id=request.session["account_id"])
            form.date = request.POST["date"]
            if Decimal(request.POST["amount"])>0:
                form.amount = Decimal(request.POST["amount"]) * -1
            else:
                form.amount = Decimal(request.POST["amount"])
            # form.payee_payer = request.POST["payee_payer"]
            form.move_to_account = request.POST["move_to_account"]#in the form info is sended as queryset but the model accept an int 
            # form.event = request.POST["event"]
            form.message = request.POST["message"]
            form.save()
            # return render(request, 'transaction_done.html', {"accont_id":account_id})
            return render(request, "transaction_done.html", {'movement':True, "account_id":request.session['account_id']})
        else:
            return render(request, "movements_form.html", {"form":form, "account_id":request.session["account_id"]})
            print("form is not valid")
        
    
    
    form = Movement_form(current_account)#the parameter current account is passed to the init for rendering the options in move_to_account
    return render(request, "movements_form.html", {"form":form, "account_id":request.session["account_id"]})#the account_id passed here is for the redirect link

def pay_form(request):#Account id is sended using seccions, it is saved in account_id dictionary key and get it using request.session["account_id"]
  
    if request.method=="POST":

        form=Pay_form(request.POST)

        if form.is_valid():

            form = form.save(commit = False)
            account_id = Account_value.objects.get(id=request.session["account_id"])
            form.account_id = account_id
            form.date = request.POST["date"]
            if Decimal(request.POST["amount"])<0:#change the amount to positive if curstomer insert a negative number, 
                #next if handle wheter it shold be positive or negative
                print("got the negative number")
                form.amount =Decimal(request.POST["amount"]) * -1
            if request.POST["event"] != "deposit":#we get allways a positive, so if there is not a deposit we change it to negative
                form.amount *= -1
            print(type(form.amount))
            form.payee_payer = request.POST["payee_payer"]
            # form.move_to_account = request.POST["move_to_account"]
            form.event = request.POST["event"]
            print("event is:", request.POST['event'], "---", type(request.POST['event']))
            form.message = request.POST["message"]
            form.save()
            # return render(request, 'transaction_done.html', {"accont_id":account_id})
            return render(request, "transaction_done.html", {'movement':False, "account_id":request.session['account_id'], "event":request.POST['event']})
        else:#send the form again in case of errors
            print("form is not valid")
            return render(request, "pay_form.html", {"form":form, "account_id":request.session["account_id"]})

    movements_form = Pay_form()
    return render(request, "pay_form.html", {"form":movements_form, "account_id":request.session["account_id"]})

def edit_pay_form(request, id):
    current_obj = get_object_or_404(Movements, id=id)
    

    if request.method == 'POST':
        form = Pay_form(request.POST, instance=current_obj)
        if form.is_valid():
            form = form.save(commit = False)
            account_id = Account_value.objects.get(id=request.session["account_id"])
            form.account_id = account_id
            form.date = request.POST["date"]
            if Decimal(request.POST["amount"])<0:#change the amount to positive if curstomer insert a negative number, 
                #next if handle wheter it shold be positive or negative
                print("got the negative number")
                form.amount =Decimal(request.POST["amount"]) * -1
            if request.POST["event"] != "deposit":#we get allways a positive, so if there is not a deposit we change it to negative
                form.amount *= -1
            print(type(form.amount))
            form.payee_payer = request.POST["payee_payer"]
            # form.move_to_account = request.POST["move_to_account"]
            form.event = request.POST["event"]
            form.message = request.POST["message"]
            form.save()
            # return render(request, 'transaction_done.html', {"accont_id":account_id})
            return redirect("/transaction_done/")
            
        else:
            print("form is not valid")
            return render(request, "pay_form.html", {"form":form, "account_id":request.session["account_id"]})
   
    form = Pay_form(instance=current_obj, initial={"amount":current_obj.amount*-1})#the initial shows the amount as possitive number 
    return render(request, "pay_form.html", {"form":form, "account_id":request.session["account_id"]})
    
def edit_movement_form(request, id):
    current_obj = get_object_or_404(Movements, id=id)#we get the object to render it in the form call
    current_account = get_object_or_404(Account_value, id = request.session["account_id"])#Need this object to the move_to_account field rendered in init

    if request.method == 'POST':
        form = Pay_form(request.POST, instance=current_obj)
        if form.is_valid():
            print("form is valid")

            form = form.save(commit = False)
            form.account_id = Account_value.objects.get(id = request.session["account_id"])#Account_value.objects.get(id=request.session["account_id"])
            form.date = request.POST["date"]
            if Decimal(request.POST["amount"])>0:
                form.amount = Decimal(request.POST["amount"]) * -1
            else:
                form.amount = Decimal(request.POST["amount"])
            form.move_to_account = request.POST["move_to_account"]#in the form info is sended as queryset but the model accept an int 
            form.message = request.POST["message"]
            form.save()
            return redirect("/transaction_done/")
            
        else:
            print("form is not valid")
            return render(request, "movements_form.html", {"form":form, "account_id":request.session["account_id"]})
   
    form = Movement_form(current_account ,instance=current_obj, initial={"amount":current_obj.amount*-1})#the initial shows the amount as possitive number 
    return render(request, "movements_form.html", {"form":form, "account_id":request.session["account_id"]})

def transaction_done(request):
    context = {"account_id":request.session["account_id"]}
    return render(request, "transaction_done.html", context)

def account_deleted(request):
    return render(request, "account_deleted.html")

def account_created(request):
    return render(request, "account_created.html")

def upload_file(request):#TODO Read about a faster way to access datebase only once and save all the events, I have a video abount that named bulk update
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print("fffffffffffff", request.POST['bank'])
            statements = accounts.read_tiliote.extract_info(request.FILES['file'], request.user, request.POST['year'], request.POST['bank'])
            statement_list = list()
            for statement in statements:
                print("view", statement)
                new_form = UploadFileForm(request.POST, request.FILES).save(commit = False)
                account_id = Account_value.objects.get(id=request.session["account_id"])#TODO I can merge this line with the next
                new_form.account_id = account_id
                # print(f"{request.POST['year']}-{statement[0][3:5]}-{statement[0][:2]}")
                
                
                if request.POST['bank'] == "nordea":
                    #Date
                    new_form.date = f"{request.POST['year']}-{statement[0][3:5]}-{statement[0][:2]}"
                    #Amount
                    if statement[3][-1] == "-":
                        new_form.amount = Decimal(statement[3][:-1].replace(".","").replace(",",".")) *-1
                    else:
                        new_form.amount = Decimal(statement[3][:-1].replace(".","").replace(",","."))
                    #Message
                    new_form.message = statement[1]
                    
                    statement_list.append(new_form)
    
                elif request.POST['bank'] == "sp":
                    #Date
                    new_form.date = f"{request.POST['year']}-{statement[0][2:4]}-{statement[0][:2]}"
                    #Amount
                    if statement[2][-1] == "-":
                        new_form.amount = Decimal(statement[2][:-1].replace(".","").replace(",",".")) *-1
                    else:
                        new_form.amount = Decimal(statement[2][:-1].replace(".","").replace(",","."))
                    #Message
                    new_form.message = statement[1]
                    
                    statement_list.append(new_form)
            
            #Write movements in database
            for i in statement_list:
                i.save()
            return redirect("/readed_successfully/")
        else:
            return render(request, "upload_file.html", {"form":form})
    context = UploadFileForm()
    return render(request, "upload_file.html", {"form":context})

def readed_successfully(request):
    context = {"account_id":request.session["account_id"]}
    return render(request, "readed_successfully.html", context)













