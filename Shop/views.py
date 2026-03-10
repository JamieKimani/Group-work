from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')
def employee_login(request):
    return render(request, 'employee_login.html')
def register(request):
    return render(request, 'register.html')
def checkout(request):
    return render(request, 'checkout.html')