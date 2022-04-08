from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserDetails(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    #firstname
    first_name = models.CharField(max_length=30, null=True, blank=True)
    #last_name
    last_name = models.CharField(max_length=30, null=True, blank=True)
    #email
    email = models.EmailField(null=True, blank=True)
    #username
    username = models.CharField(max_length=30, null=True, blank=True)
    phone_number = models.CharField(max_length=15, default="02X-XXX-XXXX")
    profile_picture = models.ImageField(default="user.png", null=True, blank=True)


    def __str__(self):
        return self.user.first_name + ' - ' + self.phone_number 