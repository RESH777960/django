from django.urls import path,include
from .views import create_product,list_product,create_brand,list_brand,edit_items,product_detail,delete_product
urlpatterns = [


    path("products",create_product,name="crate_product"),
    path("items",list_product,name="fetchitems"),
    path("brand",create_brand,name="crate_brand"),
    path("brandlist",list_brand,name="fetchbrand"),
    path("item/change/<int:id>",edit_items,name="change"),
    path("item/<int:id>",product_detail,name="product_detail"),
    path("item/remove/<int:id>",delete_product,name="remove")






]