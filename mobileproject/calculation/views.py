from django.shortcuts import render

# Create your views here.
#view for getting addition.html



def get_addition_page(request):
    return render(request,"addition.html")


def get_subtraction_page(request):
    return render(request,"stractionfile.html")





def calculate(request):
    num1=request.POST.get('num1')
    num2=request.POST.get("num2")
    res=int(num1)+int(num2)
    print(res)
    return render(request,"addition.html")

def subtraction_page(request):
    num3=request.POST.get('num3')
    num4=request.POST.get("num4")
    r=int(num3)-int(num4)
    print(r)
    context={}
    context["result"]=r
    return render(request,"stractionfile.html",context)