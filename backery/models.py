from random import choices
from turtle import mode
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Cakes(models.Model):
    name = models.CharField(max_length=100)
    description=models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_onn = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
class Biscuit(models.Model):
    taste_choices=(('sweet','sweet'),('salty','salty'))
    name=models.CharField(max_length=100)
    taste=models.CharField(choices=taste_choices,max_length=10)
    price =models.DecimalField( max_digits=5,decimal_places=2)
    created_on= models.DateTimeField(auto_now= True)
    def __str__(self):
        return self.name


