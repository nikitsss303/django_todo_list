from django.shortcuts import render, redirect
from authorization_app.models import Todo 


# Create your views here.
def list_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'delete-action':
            todo_id = request.POST.get('todo_id')
            todo = Todo.objects.filter(id=todo_id, user_id=request.user)

            if todo:
                todo.delete()
            return redirect('list_app:list')

    filtered_tasks = Todo.objects.filter(user_id=request.user.id)
    return render(request, 'list.html', {
        'user_name':request.user,
        'todos':filtered_tasks
    })


def create_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        title = request.POST.get('title')
        description = request.POST.get('description')
        user_id = request.user

        todo = Todo.objects.create(
            title=title, 
            description=description, 
            user_id=user_id
        )
        
        todo.save()
        
        if action == 'create':
            return render(request, 'create.html', {'user_name':request.user})
        elif action == 'create_and_exit':
            return redirect('list_app:list')
        else:
            return redirect('list_app:list')
        
    return render(request, 'create.html', {'user_name':request.user})