
from django.urls import path
from .views import index,create_todo

urlpatterns = [
    path('', index,name="home"),
    path('create',create_todo,name="create"),

]