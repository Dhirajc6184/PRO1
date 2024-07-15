from django.shortcuts import render,redirect
from home.models import Task

# Create your views here.
def home(request):
    if request.method=='POST':
        title=request.POST['Task-name']
        desc=request.POST['Task-desc']
        ins=Task(Task_name=title,Task_desc=desc)
        ins.save()
    return render (request,'home.html')

def see(request):
    var=Task.objects.all().order_by('Task_name')
    context={'Task':var}
    return render (request,'see.html',context)

def delete(request, id):
    var=Task.objects.get(pk=id)
    var.delete()
    return redirect('see')

def search(request):
    if request.method=='POST':
        search=request.POST['search']
        x=Task.objects.filter(Task_name__contains=search)
        context={'search':search,'x':x}
    return render (request,'see1.html',context)