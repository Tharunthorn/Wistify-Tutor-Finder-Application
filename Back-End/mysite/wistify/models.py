from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)

    LEARNER = 'learner'
    TUTOR = 'tutor'
    ROLE_CHOICES = [
        (LEARNER, 'Learner'),
        (TUTOR, 'Tutor'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=LEARNER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

class Learner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

