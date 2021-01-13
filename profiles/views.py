from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from .models import Profile
from .forms import SignUpForm
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.

#we create views using classes importing as parameter the functions
class HomeView(TemplateView):
    template_name = 'index.html'#template_name function save the url address.

class SignUpView(CreateView):
    template_name = 'profile_form.html'
    success_message = "Your profile was created successfully"
    #was before
    model = Profile
    form_class = SignUpForm

    def form_valid(self, form):
        '''
        In this part if the form is valid we save what we get from it and use authenticate for the user to sign in affter sign up and redirect to index
        '''
        form.save()
        user = form.cleaned_data.get('username')#save in user the user data got from this class form
        password = form.cleaned_data.get('password1')#save in password the password data got from this class form
        user = authenticate(username=user, password=password)#save the user and pasword in the variable user
        login(self.request, user)#Pass the user data to the login function
        return redirect('/')#Come back to the home page

class SignInView(LoginView):
    template_name = 'templates/sign_in.html'

class SignOutView(LogoutView):
    pass