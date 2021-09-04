from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=17)
    def __str__(self):
        return self.user.username
class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=17)
    pincode = models.IntegerField()
    address = models.TextField()
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    landmark = models.CharField(max_length=20)
    address_type = models.CharField(max_length=10)
class Card(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name_on_card = models.CharField(max_length=20)
    card_number = models.CharField(max_length=16)
    exp_date = models.CharField(max_length=5)
    def __str__(self):
        return self.name_on_card