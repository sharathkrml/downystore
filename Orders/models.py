from django.db import models
from Products.models import Product
from django.contrib.auth.models import User
from Accounts.models import Address
# Create your models here.

class Cart(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    @property
    def total_price(self):
        return int(self.product_id.price)*self.quantity



class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_ids = models.ManyToManyField(Cart)
    address_id = models.ForeignKey(Address, on_delete=models.CASCADE)
    delivery_status = models.CharField(max_length=30)
    order_date = models.DateTimeField(auto_now=True)
    total_price = models.IntegerField()
