
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy,reverse
from django.views.generic import ListView,DetailView,DeleteView
from .models import Task,Category
from .forms import TaskForm,CategoryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView

class TaskListView(View):
    template_name = 'task_list.html'

    def get(self, request):
        tasks = Task.objects.all()
        return render(request, self.template_name, {'tasks': tasks})
    
class CompletedTaskListView(ListView):
    model = Task
    template_name = 'completed.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(completed=True)
    
class RemainingTaskListView(ListView):
    model = Task
    template_name = 'remaining.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(completed=False)
        
class TaskCreateView(LoginRequiredMixin, FormView):
    template_name = 'add_task.html'

    def get(self, request):
        form = TaskForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.instance.user = self.request.user
            form.save()
            return redirect('home')
        return render(request, self.template_name, {'form': form})
    
class CategoryCreateView(View):
    template_name = 'category_form.html'

    def get(self, request):
        form = CategoryForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
        return render(request, self.template_name, {'form': form})

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'
    pk_url_kwarg = 'task_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class ToggleCompleteView(View):
    def get(self,request,task_id):
        task = Task.objects.get(id=task_id)
        print(task)
        if task:
            task.completed = not task.completed
            task.save()
        return redirect('home')

class TaskDeleteView(View):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    context_object_name = 'task'
    pk_url_kwarg = 'task_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'delete.html', {
        "task": task,
    })

def remove_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if task:
        task.delete()
        return redirect('home')   

