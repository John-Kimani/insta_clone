from django.shortcuts import render
from .forms import LoginForm

def login_user(request):
    return render(request, 'login.html')
