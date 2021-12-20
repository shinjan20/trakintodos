from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

# Create your models here.

completion_choices=[
    (True,'Yes'),
    (False,'No')
]

class User(AbstractUser):
    email=models.EmailField(unique=True,null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
        
class Todo(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    is_completed = models.BooleanField(choices=completion_choices,default=False)
    user = models.ForeignKey(User,on_delete=CASCADE)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title