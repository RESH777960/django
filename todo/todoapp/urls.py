
from django.urls import path
from .views import index,create_todo,list_all_todos,delete_todo,update_todo

urlpatterns = [
    path('', index,name="home"),
    path('create',create_todo,name="create"),
    path('list',list_all_todos,name="list"),
    path('delete/<int:id>',delete_todo,name='delete_todo'),
    path('update/<int:id>',update_todo,name="update_todo"),

]