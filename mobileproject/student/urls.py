from django.urls import path
from .views import register,login,index,feedback,get_reg
urlpatterns = [
    path("register",register,name="signin"),
    path("login",login,name="login"),
    path("index",index,name="home"),
    path("feedback",feedback,name="response"),
    path("getreg",get_reg,name="getreg")


]