from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """A person who is allowed to be participated in the application. """
    
    # Username is unnecessary for this application
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
    """A user who is looking for a suitable tutor. """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Tutor(models.Model):
    """A user who has a responsibility to dedicate a subject to a learner. """
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    
class Video(models.Model):
    """An opportunity for the tutor to promoting with a video url. """
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, blank=False, null=False)
    url = models.URLField(max_length=200, blank=False, null=False)
    
class Tag(models.Model):
    """A field or an area that a tutor is master. """
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, blank=False, null=False)
    area = models.CharField(max_length=100, blank=False, null=False)
    
class Rating(models.Model):
    """Provide a learner for an opportunity to rate and comment tutor's capability. """
    star = models.FloatField(blank=False, null=False)
    review = models.CharField(blank=True, null=True, max_length=300)
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    
