from django.shortcuts import render, get_object_or_404, redirect
from .forms import Create_account_form, Pay_form, Movement_form
from .models import Account_value, Movements
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from decimal import Decimal

# Create your views here.


# def view_accounts(request):

#     current_user = request.user

#     account = Account_value.objects.get(id=current_user.id)
#     return render(request, "view_accounts.html", {"user_account":account})

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
class create_account(CreateView):
    template_name = "account_value_form.html"
    # success_message = "Your account was created successfully"
    model = Account_value
    # form_class = Create_account_form
    fields = ['user', 'account_name', 'account_value', 'info', 'save_percent', 'saving_time']

    def form_valid(self, form):
        form.save()
        return redirect("/view_accounts/")


def movements_form(request, id):#account id is sended using the parameter through url

    if request.method=="POST":
        print("post done")

        form=Movement_form(request.POST)

        if form.is_valid():
            print("form is valid")

            form = form.save(commit = False)
            form.account_id = Account_value.objects.get(id = id)#Account_value.objects.get(id=request.session["account_id"])
            form.date = request.POST["date"]
            form.amount = Decimal(request.POST["amount"])
            # form.payee_payer = request.POST["payee_payer"]
            form.move_to_account = request.POST["move_to_account"]
            # form.event = request.POST["event"]
            form.message = request.POST["message"]
            form.save()
            return render(request, "thanks.html")

    movements_form = Movement_form()
    return render(request, "movements_form.html", {"p_m_form":movements_form})

def pay_form(request):#Account id is sended using seccions, it is saved in account_id dictionary key and get it using request.session["account_id"]
  
    if request.method=="POST":

        form=Pay_form(request.POST)

        if form.is_valid():

            form = form.save(commit = False)
            form.account_id = Account_value.objects.get(id=request.session["account_id"])
            form.date = request.POST["date"]
            form.amount = Decimal(request.POST["amount"])
            print(type(form.amount))
            form.payee_payer = request.POST["payee_payer"]
            # form.move_to_account = request.POST["move_to_account"]
            form.event = request.POST["event"]
            form.message = request.POST["message"]
            form.save()
            return render(request, "thanks.html")

    movements_form = Pay_form()
    return render(request, "pay_form.html", {"p_m_form":movements_form})







