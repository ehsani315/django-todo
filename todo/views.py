from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.

def index(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', context={'todos': todos})

def create(request):
    if request.method != 'POST':
        return JsonResponse({'message': 'this page just allow post method'})
    title = request.POST['title']
    Todo.objects.create(title=title, status=False)
    return redirect('todo:index')

def update(request, id):
    try:
        todo = Todo.objects.get(id=id)
    except:
        return JsonResponse({'message': f'the object with id {id} not found'})
    todo.status = not todo.status
    todo.save()
    return redirect('todo:index')

def delete(request, id):
    try:
        todo = Todo.objects.get(id=id)
    except:
        return JsonResponse({'message': f'the object with id {id} not found'})
    
    todo.delete()
    return redirect('todo:index')