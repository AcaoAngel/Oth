from django.shortcuts import render
from .forms import Contact_form
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def contact(request):

    if request.method=="POST":

        form=Contact_form(request.POST)
        
        if form.is_valid:

            name=request.POST["name"]
            subject=request.POST["subject"]
            email=request.POST["email"]
            content="{}\n{}\n{}".format(name, email, request.POST['content'])
            email_from=settings.EMAIL_HOST_USER
            recipient_list=["pythondevelopper0@gmail.com", "angel.acao92@gmail.com"]
            try:#Shows max 6 characters of the name in Gmail preview subject field 
                name_subject = name[0:6] + " " + subject#using this variable we show the name and subject in the gmail preview subject field.
            except IndexError:
                name_subject = name + " " + subject
    
            send_mail(name_subject, content, email_from, recipient_list)
    
            return render(request, "thanks.html")


    contact_form=Contact_form()
    return render(request, "contact.html", {'c_form':contact_form})
