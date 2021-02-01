from django.shortcuts import render, get_object_or_404, redirect
from .forms import Create_account_form, Pay_movement_form
from .models import Account_value, Movements
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.


# def view_accounts(request):

#     current_user = request.user

#     account = Account_value.objects.get(id=current_user.id)
#     return render(request, "view_accounts.html", {"user_account":account})

class view_accounts(ListView):

    def get_queryset(self):
        if self.request.user.is_authenticated:
            self.template_name = "view_accounts.html"
            print("getting into authenticated")
            current_user_account = Account_value.objects.filter(user_id=self.request.user.id)

            return current_user_account
            
        print("getting in else")
        self.template_name = "access_denied_accounts.html"


def account_detail(request, id):
    # print("************args",id)
    print("*******ID***********", type(id), "******", id)

    account = Account_value.objects.get(id=id)
    movements = Movements.objects.filter(account_id_id=id)
    for i in movements:
        print(i)
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


def movements_form(request):

    if request.method=="POST":

        form=Pay_movement_form(request.POST)

        if form.is_valid:

            account_id = request.POST["account_id"]
            date = request.POST["date"]
            amount = request.POST["amount"]
            payee_payer = request.POST["payee_payer"]
            event = request.POST["event"]
            message = request.POST["message"]
            date = request.POST["date"]
            return render(request, "thanks.html")

    movements_form = Pay_movement_form()
    return render(request, "movements_form.html", {"p_m_form":movements_form})








