from django.shortcuts import render,redirect
from .forms import ProductCreateFrom,BrandCreateFrom
from .models import Product

# Create your views here.
#view for create and list all products
#if method is get this view will return all objects from products models
#if method is post will createa new objectbinside models

def create_product(request):


    form=ProductCreateFrom()
    context={}
    context["form"]=form
    if request.method =="POST" :
        form=ProductCreateFrom(request.POST,files=request.FILES)
        if form.is_valid:
            form.save()
            return redirect("fetchitems")



    return render(request,"product_create.html",context)


#view for listing all products


def list_product(request):

    mobiles=Product.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"product_list.html",context)










