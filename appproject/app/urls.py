from django.urls import path
from app.views import index,create,list_todos


urlpatterns=[
    path("home",index,name="home"),
    path("creates",create,name="create"),
    path("lists",list_todos,name="lists1")
]