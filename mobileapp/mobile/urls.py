from django.urls import path,include
from .views import create_product,list_product
urlpatterns = [


    path("products",create_product,name="crate_product"),
    path("items",list_product,name="fetchitems")



]