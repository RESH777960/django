from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def register(request):
    return render(request,"register.html")


def login(request):
    return render(request,"login.html")


def index(request):
    return render(request,"index.html")


def feedback(request):
    return render(request,"feedback.html")
def get_reg(request):
    first_name=request.POST.get('fname')
    email = request.POST.get('email')
    user_name = request.POST.get('uname')
    password = request.POST.get('password')
    print(first_name,email,user_name,password)
    return render(request,"index.html")


