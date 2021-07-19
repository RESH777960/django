from calculation.views import get_addition_page,calculate,subtraction_page,get_subtraction_page
from django.urls import path

urlpatterns=[
    
    path("add",get_addition_page,name="getadd"),
    path("calcu",calculate,name="add"),
    path("sub",get_subtraction_page,name="sub1"),
    path("subtra",subtraction_page,name="sub"),
    
]