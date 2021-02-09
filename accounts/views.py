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

    account = Account_value.objects.get(id=id)
    print(type(account.id), account.id)
    request.session["account_id"] = id 
    movements = Movements.objects.filter(account_id_id=id)

    context = {'account':account, 'movements':movements}

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

    # if request.method=="GET":
    #     current_account_id = get_object_or_404(Account_value, id = request.session["account_id"])
    #     print("got in GET",current_account_id)
        

    if request.method=="POST":
        print("post done")

        form=Movement_form(request.POST, request.user)

        if form.is_valid():
            print("form is valid")

            form = form.save(commit = False)
            form.account_id = Account_value.objects.get(id = request.session["account_id"])#Account_value.objects.get(id=request.session["account_id"])
            form.date = request.POST["date"]
            form.amount = Decimal(request.POST["amount"]) * -1
            # form.payee_payer = request.POST["payee_payer"]
            form.move_to_account = request.POST["move_to_account"]
            # form.event = request.POST["event"]
            form.message = request.POST["message"]
            form.save()
            # return render(request, 'transaction_done.html', {"accont_id":account_id})
            return redirect("/transaction_done/")
        else:
            return render(request, "pay_form.html", {"form":form})
            print("form is not valid")
        
    current_account_id = get_object_or_404(Account_value, id = request.session["account_id"])
    print("current account id is a ",type(current_account_id.id))
    # form = Movement_form(initial={"account_id":Account_value.objects.get(id = request.session["account_id"])})
    form = Movement_form(request.user, request.session["account_id"])
    return render(request, "movements_form.html", {"form":form})

def pay_form(request):#Account id is sended using seccions, it is saved in account_id dictionary key and get it using request.session["account_id"]
  
    if request.method=="POST":

        form=Pay_form(request.POST)

        if form.is_valid():

            form = form.save(commit = False)
            account_id = Account_value.objects.get(id=request.session["account_id"])
            form.account_id = account_id
            form.date = request.POST["date"]
            if request.POST["event"] != "deposit":
                form.amount = Decimal(request.POST["amount"]) * -1
            else:
                form.amount = Decimal(request.POST["amount"])
            print(type(form.amount))
            form.payee_payer = request.POST["payee_payer"]
            # form.move_to_account = request.POST["move_to_account"]
            form.event = request.POST["event"]
            form.message = request.POST["message"]
            form.save()
            # return render(request, 'transaction_done.html', {"accont_id":account_id})
            return redirect("/transaction_done/")
        else:#send the form again in case of errors
            return render(request, "pay_form.html", {"form":form})

    movements_form = Pay_form()
    return render(request, "pay_form.html", {"form":movements_form})

def transaction_done(request):

    context = {"account_id":request.session["account_id"]}
    return render(request, "transaction_done.html", context)



def account_created(request):

    return render(request, "account_created.html")




