from django.shortcuts import render, get_object_or_404, redirect
from .forms import Create_account_form, Pay_form, Movement_form
from .models import Account_value, Movements
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.models import User
from decimal import Decimal

# Create your views here.




class view_accounts(ListView):

    def get_queryset(self):
        account = Account_value.objects.all()
            
        if self.request.user.is_authenticated:
            self.template_name = "view_accounts.html"
            current_user_account = Account_value.objects.filter(user_id=self.request.user.id)
            return current_user_account
            
        self.template_name = "access_denied_accounts.html"


def account_detail(request, id):
    print("loading from account detail")
   
    account = Account_value.objects.get(id=id)
    print(type(account.id), account.id)
    request.session["account_id"] = id 
    movements = Movements.objects.filter(account_id_id=id)

    context = {'account':account, 'movements':movements}
        
    return render(request, "account_detail.html", context)

def sure_delete(request, id, movement_id):
    print("loading from sure delete")
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


    context = {'account':account, 'movements':movements, 'sure_delete':True, "deleting_movement":deleting_movement}

    return render(request, "account_detail.html", context)


#------------------------------------------------------------------------------------
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

# class create_account(CreateView):
#     template_name = "account_value_form.html"
#     # success_message = "Your account was created successfully"
#     model = Account_value
#     # form_class = Create_account_form
#     fields = ['user', 'account_name', 'account_value', 'info', 'save_percent', 'saving_time']

#     def form_valid(self, form):
#         form.save()
#         return redirect("/")


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
            return redirect("/transaction_done/")
        else:
            return render(request, "pay_form.html", {"form":form, "account_id":request.session["account_id"]})
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
            form.message = request.POST["message"]
            form.save()
            # return render(request, 'transaction_done.html', {"accont_id":account_id})
            return redirect("/transaction_done/")
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



def account_created(request):

    return render(request, "account_created.html")


