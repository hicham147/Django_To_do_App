from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages



def home(request):
    context = Task.objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully added')
            return redirect('home')
    else:
        form = TaskForm()


    return render(request,"main.html",{"task":context,"form":form})
