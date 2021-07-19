from django.db import models

# Create your models here.




class Todos(models.Model):
    task_name=models.CharField(max_length=150)
    status=models.CharField(max_length=15,default='notcompleted')
    user=models.CharField(max_length=140)
    date=models.DateField(auto_now=True)



    def __str__(self):
        return self.task_name
# todo=Todos(task_name="gaspayment",status="notcompleted",user="reshma")
# todo.save()
