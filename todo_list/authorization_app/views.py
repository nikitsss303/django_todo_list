from django.shortcuts import render, HttpResponse

# Create your views here.
def login_view(request):
    return HttpResponse('login_view')


def logout_view(request):
    return HttpResponse('logout_view')


def signup_view(request):
    return HttpResponse('signup_view')