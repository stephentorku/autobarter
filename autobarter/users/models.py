from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserDetails(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)


    def __str__(self):
        return self.user.first_name + ' - ' + self.phone_number 