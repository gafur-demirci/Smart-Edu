from django.shortcuts import render

# Create your views here.
def user_login(request):
    return render(request, 'login.html')

def user_register(request):
    return render(request, 'register.html')

def user_dashboard(request):
    pass

def user_logout(request):
    pass