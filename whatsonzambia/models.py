from audioop import reverse
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from .managers import CustomUserManager
from PIL import Image


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email address'), unique=True)
    fullname = models.CharField(max_length=100)
    contact = PhoneNumberField(null=False, blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Post(models.Model):
    title = models.CharField(verbose_name='Event Name', max_length=100)
    content = models.TextField(verbose_name='More Information', max_length=250)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    charge = models.CharField(verbose_name='Charges', max_length=100)
    venue = models.CharField(verbose_name='Event Venue', max_length=100)
    event_day = models.CharField(verbose_name='Event Day',max_length=100)
    event_date = models.CharField(verbose_name='Event Date', max_length=50)
    town = models.CharField(verbose_name='Town/City', max_length=100)
    event_time = models.TimeField(verbose_name='Event Time',)
    post_image = models.ImageField(verbose_name='Uploadadvert Image', upload_to='post_img', null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self):
        super().save()

        img = Image.open(self.post_image.path)

        if img.height > 350 or img.width > 700:
            output_size = (350, 700)
            img.thumbnail(output_size)
            img.save(self.post_image.path)        

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class PostFeature(models.Model):
    ft_title = models.CharField(verbose_name='Event Name', max_length=100)
    ft_content = models.TextField(verbose_name='More Information', max_length=250)
    ft_date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    ft_charge = models.CharField(verbose_name='Charges',max_length=100)
    ft_venue = models.CharField(verbose_name='Venue',max_length=100)
    ft_event_day = models.CharField(verbose_name='Event Day',max_length=100)
    ft_event_date = models.CharField(verbose_name='Event Date',max_length=50)
    ft_town = models.CharField(verbose_name='Town/City', max_length=100)
    ft_event_time = models.TimeField(verbose_name='Event Time')
    ft_post_image = models.ImageField(verbose_name='Upload Advert Image', upload_to='feat_img', null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self):
        super().save()

        img = Image.open(self.ft_post_image.path)

        if img.height > 350 or img.width > 700:
            output_size = (350, 700)
            img.thumbnail(output_size)
            img.save(self.ft_post_image.path)          

    def get_absolute_url(self):
        return reverse('whatsonzambia-home')