from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    USER_TYPES=[
        ('admin','Admin'),
        ('user','User'),
    ]
    
    full_name=models.CharField(max_length=100, null=True)
    user_types=models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.full_name
    
class Category(models.Model):
    name=models.CharField(max_length=100, null=True)
    description=models.TextField(null=True)

    def __str__(self):
        return self.name
    
class Recipie(models.Model):
    title=models.CharField(max_length=100, null=True) 
    description=models.TextField(max_length=100 ,null=True)
    ingredients=models.CharField(max_length=100, null=True)
    instructions=models.CharField(max_length=100, null=True)
    image=models.ImageField(null=True, upload_to="Pics")
    category=models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    created_by=models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE,related_name='Created_user')
    created_at=models.DateField(auto_now_add=True, null=True)
    updated_at=models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.title
    