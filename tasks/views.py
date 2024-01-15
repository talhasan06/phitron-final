
from django.shortcuts import render, redirect,get_object_or_404
from django.views import View
from django.urls import reverse_lazy,reverse
from django.views.generic import ListView,DetailView
from .models import Task,Category
from .forms import TaskForm,CategoryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import get_user_model

class TaskListView(View):
    template_name = 'task_list.html'

    def get(self, request):
        user = request.user
        tasks = Task.objects.filter(user=user)
        return render(request, self.template_name, {'tasks': tasks})
    
class CompletedTaskListView(ListView):
    model = Task
    template_name = 'completed.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user,completed=True)
    
class RemainingTaskListView(ListView):
    model = Task
    template_name = 'remaining.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user,completed=False)
        
class TaskCreateView(LoginRequiredMixin, FormView):
    template_name = 'add_task.html'
    success_url = '/'
    def get(self, request):
        form = TaskForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.instance.user = self.request.user
            task = form.save() 

            email_subject = 'New task created'
            task_title=form.cleaned_data['title']
            email_body=render_to_string('task_created_confirmation.html',{'task_title':task_title})
            email = EmailMultiAlternatives(email_subject,'',to=[task.user.email])
            email.attach_alternative(email_body,"text/html")
            email.send()
            return super().form_valid(form)
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
        task = get_object_or_404(Task, id=task_id)
        print(task)

        if task:
            task.completed = not task.completed
            task.save()
            if task.completed:
                User = get_user_model()

                email_subject = 'Task Completed'
                task_title=task.title
                email_body=render_to_string('task_completed_confirmation.html',{'task_title':task_title})
                email = EmailMultiAlternatives(email_subject,'',to=[task.user.email])
                email.attach_alternative(email_body,"text/html")
                email.send()
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

