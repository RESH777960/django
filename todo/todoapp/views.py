from django.shortcuts import render,redirect
from todoapp.forms import TodoModelForm
# from .models import Todos
from todoapp.models import Todos


# Create your views here.
def index(request):
    return render(request,'index.html')
def create_todo(request):
    if request.method=="GET":
        form = TodoModelForm()

        context={}
        context["form"]=form
        return render(request, 'createtodo.html',context)
    elif request.method=="POST":
        form=TodoModelForm(request.POST)
        if form.is_valid():
            # takname=form.cleaned_data.get("task_name")
            # user=form.cleaned_data.get("user")
            # status=form.cleaned_data.get("status")
            # todo=Todos(task_name=takname,status=status,user=user)
            form.save()
            return render(request,"index.html")

def list_all_todos(request):
    todos=Todos.objects.all()
    context={}
    context["todos"]=todos
    return render(request,"listalltodos.html",context)
def delete_todo(request,id):
    todo=Todos.objects.get(id=id)
    todo.delete()
    return redirect("list")
def update_todo(request,id):
#get and post functions
    todo=Todos.objects.get(id=id)
    # instance={
    #     "task_name":todo.task_name,
    #     "user":todo.user,
    #     "status":todo.status,
    # }
    form=TodoModelForm(instance=todo)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=TodoModelForm(instance=todo,data=request.POST)
        if form.is_valid():
            # task_name=form.cleaned_data.get("task_name")
            # user= form.cleaned_data.get("user")
            # status= form.cleaned_data.get("status")
            # todo.task_name=task_name
            # todo.user=user
            # todo.status=status
            form.save()
            return redirect("list")

    return render(request,"edittodo.html",context)





