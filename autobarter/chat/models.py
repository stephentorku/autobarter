from django.db import models
from django.contrib.auth.models import User
import datetime
from django.forms import DateField

# Create your models here.


class Chat(models.Model):
    #only buyers can start chats
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="buyer")
    #user2 is a vendor
    vendor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vendor")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.buyer.first_name, self.vendor.first_name)


class Message(models.Model):
    text = models.CharField(max_length=1000000)
    date = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return '%s - %s' % (self.sender.first_name, self.text[0:10])