from email import charset
from unicodedata import category
from django.db import models
from django.forms import CharField, DateTimeField

# Create your models here.
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def _str_(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    category = models.ForeignKey(Category, 
                    on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')

    class Meta:
        verbose_name_plural = 'News'
