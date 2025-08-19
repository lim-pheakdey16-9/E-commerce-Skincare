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
    
class brands(models.Model):
    name_kh = models.CharField(max_length=30)
    name_en = models.CharField(max_length=30)
    order = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='brand_images/', blank=True, null=True)

    def __str__(self):
        return self.name_en
    
class type(models.Model):
    name = models.CharField(max_length=30)
    order = models.IntegerField(default=1)
    def __str__(self):
        return self.name
    
class color(models.Model):
    name = models.CharField(max_length=30)
    order = models.IntegerField(default=1)
    def __str__(self):
        return self.name

class size(models.Model):
    name = models.CharField(max_length=30)
    order = models.IntegerField(default=1)
    def __str__(self):
        return self.name

class product(models.Model):    
    name = models.CharField(max_length=200, null=True) 
    type_id = models.ForeignKey(type, on_delete=models.CASCADE, null=True)    
    brand_id = models.ForeignKey(brand, on_delete=models.CASCADE, null=True)    
    color_id = models.ForeignKey(color, on_delete=models.CASCADE, null=True)    
    size_id = models.ForeignKey(size, on_delete=models.CASCADE, null=True)    
    Price = models.CharField(max_length=200, null=True) 
    image = models.ImageField(upload_to='ProductImages/')
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):         
        return f'{self.name}'  