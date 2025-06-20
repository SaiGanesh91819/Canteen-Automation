from django.db import models # type: ignore

# Create your models here.
class user_profile_data(models.Model):
    user_name = models.CharField(blank=True,null=True ,max_length=30)
    user_img = models.ImageField(blank=True,upload_to='user_images/',null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    branch = models.CharField(max_length=100, blank=True, null=True)
    reg_no = models.CharField(max_length=10, unique=True, blank=True, null=True)
