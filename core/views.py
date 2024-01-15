from django.shortcuts import render
from tasks.models import Task
# Create your views here.
def home(request):
    # data = Task.objects.all()
    return render (request,'index.html')