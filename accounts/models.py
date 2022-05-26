from email.mime import image
import imp
from django.db import models
from whatsonzambia.models import CustomUser
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.email} Profile'
