from django.shortcuts import render
from tasks.models import Task,Category

# Create your views here.
def home(request,category_slug = None):
    tasks = Task.objects.all()
    categories = Category.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        tasks = Task.objects.filter(category=category)
    categories = Category.objects.all()
    return render (request,'index.html',{'tasks':tasks,'categories':categories,'for_filter':'for_filter'})

