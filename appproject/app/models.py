from django.db import models

# Create your models here.
#closly related to database



class Todos(models.Model):
    task_name=models.CharField(max_length=15)
    status = models.CharField(max_length=15,default="not completed")
    user=models.CharField(max_length=150)
    date=models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.task_name



class Employee(models.Model):
    emp_name=models.CharField(max_length=20)
    status= models.CharField(max_length=20)
    task_name = models.CharField(max_length=20)
    date=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.emp_name

