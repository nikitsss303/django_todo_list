from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_password = request.POST.get('user_password')

        user = authenticate(request, username=user_name, password=user_password)

        print(user)

        if user is not None:
            login(request, user)
            return redirect('authorization_app:test')
        else:
            return render(request, 'login.html', {'error':'Incorrect name or password!'})
         
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('authorization_app:login')


def signup_view(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_password1 = request.POST.get('user_password1')
        user_password2 = request.POST.get('user_password2')

        if user_password1 != user_password2:
            return render(request, 'signup.html', {'error':"Passwords don't match"})
        
        if User.objects.filter(username=user_name).exists():
            return render(request, 'signup.html', {'error':"There is a user with that name"})
        
        user = User.objects.create_user(username=user_name, email='', password=user_password1)
        user.save()

        return redirect('authorization_app:login')
    return render(request, 'signup.html')


def test_view(request):
    return render(request, 'test.html')