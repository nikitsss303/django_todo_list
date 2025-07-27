from django.shortcuts import render, HttpResponse

# Create your views here.
def list_view(request):
    return HttpResponse('list_view')


def create_view(request):
    return HttpResponse('create_view')


def delete_view(request):
    return HttpResponse('delete_view')


def update_view(request):
    return HttpResponse('update_view')