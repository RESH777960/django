from django.shortcuts import render
from app.forms import TodoCreateForm
from .models import Todos
# Create your views here.
def index(request):
    return render(request,"index.html")
def create(request):



    if request.method=="GET":

        form=TodoCreateForm()
        context={}
        context["form"]=form

        return render(request,"createtodo.html",context)






    if request.method=="POST":



        form=TodoCreateForm(request.POST)
        if form.is_valid():
            taskname=form.cleaned_data.get("task_name")
            user=form.cleaned_data.get("user")
            status=form.cleaned_data.get("status")
            todos=Todos(task_name=taskname,status=status,user=user)
            todos.save()
            return render(request,"index.html")





    if request.method=="GET":

        form=TodoCreateForm()
        context={}
        context["form"]=form

        return render(request,"createtodo.html",context)






    if request.method=="POST":



        form=TodoCreateForm(request.POST)
        if form.is_valid():
            taskname=form.cleaned_data.get("task_name")
            user=form.cleaned_data.get("user")
            status=form.cleaned_data.get("status")
            todos=Todos(task_name=taskname,status=status,user=user)
            todos.save()
            return render(request,"index.html")






def list_todos(request):

    todos=Todos.objects.all()
    context={}
    context["todos"]=todos
    return render(request,"listall.html",context)






def update(request):
    pass
def delete(request):
    pass