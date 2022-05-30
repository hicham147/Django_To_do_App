from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.views.generic import UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

def home(request):
    todo_list = Task.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'Successfully added')
            return redirect('home')
    else:
        form = TaskForm()


    return render(request,"main.html",{"task":todo_list,"form":form})



class UpdateTask(SuccessMessageMixin,UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'update.html'
    success_message  = 'Your task has been updated'
    success_url  = reverse_lazy('home')


class DeleteTask(SuccessMessageMixin,DeleteView):
    model = Task
    fields = '__all__'
    template_name = 'delete.html'
    success_url  = reverse_lazy('home')
