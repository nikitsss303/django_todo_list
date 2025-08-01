from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout

# Create your views here.
def login_view(request):
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login.html')


def signup_view(request):
    return render(request, 'signup.html')