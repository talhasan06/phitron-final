from django.shortcuts import render
from tasks.models import Task,Category

# Create your views here.
def home(request,category_slug = None):
    tasks = Task.objects.filter(user=request.user)
    categories = Category.objects.filter(user=request.user).distinct()
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        tasks = tasks.filter(category=category)
        
    return render (request,'index.html',{'tasks':tasks,'categories':categories,'for_filter':'for_filter'})

