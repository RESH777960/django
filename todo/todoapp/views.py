from django.shortcuts import render
from todoapp.forms import TodoCreateForm


# Create your views here.
def index(request):
    return render(request,'index.html')
def create_todo(request):
    if request.method=="GET":
        form = TodoCreateForm()

        context={}
        context["form"]=form
        return render(request, 'createtodo.html',context)
    elif request.method=="POST":
        form=TodoCreateForm(request.POST)
        if form.is_valid():
            takname=form.cleaned_data.get("task_name")
            user=form.cleaned_data.get("user")
            status=form.cleaned_data.get("status")
            print(takname,user,status)
            return render(request,"index.html")






