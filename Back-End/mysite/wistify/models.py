from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None
    
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=30, blank=False, null=False)
    profile_picture = models.ImageField(blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']
    
class Learner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
    