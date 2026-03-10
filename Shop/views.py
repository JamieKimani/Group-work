from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def login(request):
<<<<<<< HEAD
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')
def collection(request):
    return render(request, 'collection.html')
=======
    return render(request, 'login.html')
>>>>>>> 407b0d9569c3306b04be13ba3f58bee13dec5303
