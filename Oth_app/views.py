from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def blog(request):
    return render(request, "blog.html")

def reports(request):
    return render(request, "reports.html")

def data_protection(request):
    return render(request, "data_protection.html")
