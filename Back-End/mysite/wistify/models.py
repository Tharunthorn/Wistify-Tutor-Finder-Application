from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None
    
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=20, blank=False, null=False)
    password = models.CharField(max_length=20, blank=False, null=False)
    profile_picture = models.ImageField(blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']
    
class Learner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    
class Rating(models.Model):
    star = models.FloatField(blank=False, null=False)
    review = models.CharField(max_length=300)
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    
# {
#  "star": 4,
#  "review": "Good Teaching",
#  "learner_id": 1,
#  "tutor_id": 1
# }