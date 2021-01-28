from django.shortcuts import render, get_object_or_404, redirect
from .forms import Create_account_form, Pay_movement_form
from .models import Account_value, Movements
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.models import User

# Create your views here.


# def view_accounts(request):

#     current_user = request.user

#     account = Account_value.objects.get(id=current_user.id)
#     return render(request, "view_accounts.html", {"user_account":account})

class view_accounts(ListView):
    # model = Account_value
    template_name = "view_accounts.html"

    def get_queryset(self):
        current_user = Account_value.objects.filter(user_id=self.request.user.id)
        print(current_user)
        return current_user


class account_detail(DetailView):
    template_name = "account_detail.html"
    model = Account_value

    """The view_accounts.html is sending the id of the clicked account in int format,
    since DetailView handle it as an object we must converting in the table object
    using this method
    """
    def get_object(self, queryset=None):
        return Account_value.objects.get(id=self.kwargs.get("id"))

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






    # if request.method=="POST":

    #     form=Create_account_form(request.POST)

    #     if form.is_valid:
    #         form.user = request.POST["user"]
    #         form.account_name = request.POST["account_name"]
    #         form.account_value = request.POST["account_value"]
    #         form.info = request.POST["info"]
    #         form.save_percent = request.POST["save_percent"]
    #         form.saving_time = request.POST["saving_time"]
    #         form.date = request.POST["date"]
    #         form.save()
    #         return render(request, "thanks.html")

# class SignUpView(CreateView):
#     template_name = 'profile_form.html'
#     success_message = "Your profile was created successfully"
#     #was before
#     model = Profile
#     form_class = SignUpForm

#     def form_valid(self, form):
#         '''
#         In this part if the form is valid we save what we get from it and use authenticate for the user to sign in affter sign up and redirect to index
#         '''
#         form.save()
#         user = form.cleaned_data.get('username')#save in user the user data got from this class form
#         password = form.cleaned_data.get('password1')#save in password the password data got from this class form
#         user = authenticate(username=user, password=password)#save the user and pasword in the variable user
#         login(self.request, user)#Pass the user data to the login function
#         return redirect('/')#Come back to the home page


#     create_account_form = Create_account_form()
#     print(create_account_form)
#     return render(request, "create_account.html", {"c_a_form":create_account_form})


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








