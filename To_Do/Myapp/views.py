from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.views.generic import UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

def home(request):
    # search functionaltiy
    if 'q' in request.GET or '':                                       
        q = request.GET['q']                    
        todo_list = Task.objects.filter(title__icontains=q)           
    else:
        todo_list = Task.objects.all()
     # add task functionaltiy
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully added')
            return redirect('home')
    else:
        form = TaskForm()

     # ckecked box functionaltiy
    if request.method == 'POST':
        todo_id = request.POST['todo_id']
        todo = get_object_or_404(Task, id=todo_id)
        if todo.complit:
            todo.complit = False
            todo.save()
        else:
            todo.complit = True
            todo.save()



    return render(request,"main.html",{"task":todo_list,"form":form})




# using CBV

# class UpdateTask(SuccessMessageMixin,UpdateView):
#     model = Task
#     fields = '__all__'
#     template_name = 'update.html'
#     success_message  = 'Your task has been updated'
#     success_url  = reverse_lazy('home')





# using FBV
def Update_task(request,pk):

    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully Upadated')
            return redirect('home')

    context = {"form":form}
    return render(request,'update.html',context)





class DeleteTask(SuccessMessageMixin,DeleteView):
    model = Task
    fields = '__all__'
    template_name = 'delete.html'
    success_url  = reverse_lazy('home')
    