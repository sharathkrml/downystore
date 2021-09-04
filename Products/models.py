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