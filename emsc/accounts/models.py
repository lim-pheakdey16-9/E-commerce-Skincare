from django.db import models

class user(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    dob = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.username

class brand(models.Model):
    name_kh = models.CharField(max_length=30)
    name_en = models.CharField(max_length=30)
    order = models.IntegerField(default=1)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='brand_images/', blank=True, null=True)

    def __str__(self):
        return self.name_en