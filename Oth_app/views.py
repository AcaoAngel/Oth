from django.shortcuts import render

# Create your views here.

# def home(request):
#     return render(request, "home.html")

def blog(request):
    return render(request, "blog.html")

def reports(request):
    return render(request, "reports.html")

