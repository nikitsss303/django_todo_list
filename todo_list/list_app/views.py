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
        
        elif action == 'change-action':
            todo_id = request.POST.get('todo_id')\
            
            request.session['temp_data'] = {
                'todo_id':todo_id,
            }

            return redirect('list_app:change')

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

        todo = Todo.objects.create(
            title=title, 
            description=description, 
            user_id=request.user.id
        )
        
        todo.save()
        
        if action == 'create':
            return render(request, 'create.html', {'user_name':request.user})
        elif action == 'create_and_exit':
            return redirect('list_app:list')
        else:
            return redirect('list_app:list')
        
    return render(request, 'create.html', {'user_name':request.user})


def change_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'change':
            todo_id = request.POST.get('todo_id')
            title = request.POST.get('title')
            description = request.POST.get('description')
            is_completed = request.POST.get('is_completed') == 'on'

            Todo.objects.filter(id=todo_id).update(
                title=title, 
                description=description, 
                is_completed=is_completed
            )

            return redirect('list_app:list')


    data = request.session.get('temp_data')

    todo = Todo.objects.filter(id=data['todo_id']).first()
    
    is_completed = ''
    if todo.is_completed:
        is_completed = 'checked'
    
    return render(request, 'change.html', {
                'todo_id':todo.id,
                'title':todo.title,
                'description':todo.description,
                'is_completed':is_completed,
                'user_name':request.user
            })      