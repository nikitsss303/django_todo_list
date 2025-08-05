from django.shortcuts import render, HttpResponse

# Create your views here.
def list_view(request):
    return render(request, 'list.html')


def create_view(request):
    return render(request, 'create.html')