from django.contrib.auth.models import AbstractUser
from django.db import models
import os


class CustomUser(AbstractUser):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join('Users', self.username, instance)
        return None

    STATUS = (
        ('learner', 'learner'),
        ('tutor', 'tutor'),
    )

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS, default='learner')
    description = models.TextField("Description", max_length=600, default='', blank=True)
    image = models.ImageField(default='default/user.jpg', upload_to=image_upload_to)

    def __str__(self):
        return self.username