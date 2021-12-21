from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db.models.deletion import CASCADE

# Create your models here.

completion_choices=[
    (True,'Yes'),
    (False,'No')
]

class Myaccountmanager(BaseUserManager):
    def create_user(self,email,username,password=None):
              if not email:
                  raise ValueError('Users must have an email address')
              if not username:
                  raise ValueError('Users must have an username')
              user = self.model(
                  email=email,
                  username=username,
              )
              user.set_password(password)
              user.save(using=self._db)
              return user
    
    def create_superuser(self,email,username,password):
              user = self.create_user(
                  email = email,
                  username = username,
                  password = password
              )
              user.is_admin=True
              user.is_staff=True
              user.is_superuser=True
              user.save(using=self._db)
              return user

class User(AbstractBaseUser):
    email=models.EmailField(verbose_name="email",max_length=80,unique=True)
    username=models.CharField(verbose_name="username",max_length=50)
    date_joined=models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_login=models.DateTimeField(verbose_name="last login",auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    objects=Myaccountmanager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True
        
class Todo(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True,blank=True)
    is_completed = models.BooleanField(choices=completion_choices,default=False)
    user = models.ForeignKey(User,on_delete=CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title