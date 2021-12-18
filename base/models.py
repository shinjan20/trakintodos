from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from datetime import datetime

# Create your models here.

completion_choices=[
    (True,'Yes'),
    (False,'No')
]

class Todo(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    is_completed = models.BooleanField(choices=completion_choices,default=False)
    user = models.ForeignKey(User,on_delete=CASCADE)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title