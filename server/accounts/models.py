from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  image = models.ImageField(upload_to='profile/', default='default.png')
  descriptions = models.TextField(max_length=500)
  
  def __str(self):
    return self.username
    