from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework .authtoken.models import Token
from django.conf import settings
# Create your models here.
   
class Movie(models.Model):
    hall=models.CharField(max_length=100)

    movie=models.CharField(max_length=100)

    date=models.CharField(max_length=100)

class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    title=models.CharField(max_length=100)

    body=models.TextField(max_length=100)

class Guest(models.Model):
    name=models.CharField(max_length=100)

    mobile=models.CharField(max_length=100)


class Reservation(models.Model):

    guest=models.ForeignKey(Guest,on_delete=models.CASCADE,related_name='reservation')
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE,related_name='reservation')



# @receiver(Post_Save,sender=settings.AUTHE_USER_MODEL)
# def tokencreate(sender,instance,created,**kwargs):
#     if created:
#         Token.objects.create(user=instance)
# signals
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def token_create(sender, instance, created, **kwargs):
    if created: 
        Token.objects.create(user=instance)