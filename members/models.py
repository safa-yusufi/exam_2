from django.db import models
from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField()
    phone = models.IntegerField(null=True)
    author = models.CharField(max_length=400 , null=True)
    
    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
  