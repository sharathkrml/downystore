from django.db import models
from django.utils.text import slugify
class Category(models.Model):
    name=models.CharField(max_length=30,unique=True)
    slug = models.SlugField(max_length=30,blank=True)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    price = models.CharField(max_length=10)
    image = models.CharField(max_length=200)
    slug=models.SlugField(max_length=100)
   
    @property
    def slug(self):
        return slugify(self.name)
    def __str__(self):
        return self.name