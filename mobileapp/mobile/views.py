from django.shortcuts import render, redirect
from .forms import ProductCreateFrom, BrandCreateFrom
from .models import Product,Brand


# Create your views here.
# view for create and list all products
# if method is get this view will return all objects from products models
# if method is post will createa new objectbinside models

def create_product(request):
        form = ProductCreateFrom()
        context = {}
        context["form"] = form
        if request.method=="POST":
            form = ProductCreateFrom(request.POST,files=request.FILES)
            if form.is_valid():
                form.save()
                return redirect("fetchitems")
            else:
                context["form"] = form
                #return render(request, "product_create.html", context)
        return render(request,"product_create.html",context)


# view for listing all products
def list_product(request):
    mobiles = Product.objects.all()
    context = {}
    context["mobiles"] = mobiles
    return render(request, "product_list.html", context)

def create_brand(request):
    if request.method == "GET":
        form = BrandCreateFrom()
        context = {}
        context["form"] = form
        return render(request, "Brand_CreateForm.html", context)

    if request.method == "POST":
        form = BrandCreateFrom(request.POST)
        if form.is_valid():

            brandname = form.cleaned_data.get("brand_name")
            form.save()
            return redirect("fetchbrand")
    return render(request, "Brand_CreateForm.html")

def list_brand(request):
    mobiles = Brand.objects.all()
    context = {}
    context["mobiles"] = mobiles
    return render(request, "Brandlist.html", context)

def get_object(id):
    return Product.objects.get(id=id)





def edit_items(request,*args,**kwargs):
    id=kwargs.get("id")
    product=get_object(id)
    form=ProductCreateFrom(instance=product)
    context={}
    context["form"]=form
    #return render(request,"edit_product",context)

    if request.method == "POST":
        form=ProductCreateFrom(instance=product,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("fetchitems")

    return render(request,"edit_product.html",context)

def product_detail(request,*args,**kwargs):
    id = kwargs.get("id")
    product = get_object(id)
    context = {}
    context["product"]=product


    return render(request,"product_detail.html",context)

def delete_product(request,*args,**kwargs):
    id = kwargs.get("id")
    product = get_object(id)
    product.delete()
    return redirect("fetchitems")