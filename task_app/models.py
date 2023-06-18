from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user =models.CharField(max_length=40, null=True,blank=True)
    task = models.CharField(max_length=200)
    description =models.TextField(max_length = 1000,null=True, blank=True)
    status = models.CharField(max_length=20, default='In Progress')
    file = models.FileField(upload_to="taskfiles/",max_length=150,null=True,default=None)
    
    def __str__(self):
        return self.task

# class Meta:
#     ordering =['complete']