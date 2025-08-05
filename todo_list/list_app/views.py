from django.shortcuts import render, redirect
from authorization_app.models import Todo 

# Create your views here.
def list_view(request):
    return render(request, 'list.html')


def create_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        title = request.POST.get('title')
        description = request.POST.get('description')
        user_id = request.user

        todo = Todo.objects.create(title=title, description=description, user_id=user_id)
        todo.save()
        
        if action == 'create':
            return render(request, 'create.html')
        else:
            return redirect('list_app:list')
    return render(request, 'create.html')