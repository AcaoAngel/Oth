                          
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from .models import Profile
from .forms import SignUpForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import  UserUpdateForm , ProfileUpdateForm
from django.urls import reverse

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
# Create your views here.

# we create views using classes importing as parameter the functions
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
        # messages.success(request,'Account was created for' + user)
        return redirect('/')#Come back to the home page

class SignInView(LoginView):
    template_name = 'templates/sign_in.html'

class SignOutView(LogoutView):
    pass



def profile(request):
    profile = Profile.objects.get(user=request.user)  # this is the current user who is login in.   Profile= model
    return render(request, 'templates/profile.html', {'profile': profile})


def profile_edit(request):
    profile = Profile.objects.get(id=request.user.id)
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        userupdateform= UserUpdateForm(request.POST, instance=request.user)
        profileupdateform = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=profile)

        if userupdateform.is_valid() and profileupdateform.is_valid():
            userupdateform.save()
            myprofile = profileupdateform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            success_message = "Your profile was updated successfully"
            return redirect(reverse('profiles:profile'))
    
    
    else:
        userupdateform = UserUpdateForm(instance=user)
        profileupdateform = ProfileUpdateForm(instance=profile)
    context = {
     
        'UserUpdateForm': userupdateform,
        'ProfileUpdateForm': profileupdateform
    }
  
    return render(request, 'templates/profile_edit.html',context)







#     profile = Profile.objects.get(user=request.user)

#     return render(request, 'templates/profile.html', {'profile': profile})



# def profile_edit(request):
#     profile = Profile.objects.get(user=request.user)



#     if request.method == 'POST':
#         pass


#     else :
#         UserUpdateForm = UserUpdateForm(instance=request.user)
#         ProfileUpdateForm = ProfileUpdateForm(instance=profile)
























