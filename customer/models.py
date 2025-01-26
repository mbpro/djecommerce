from django.db import models
from store.models import Product
from userauths.models import  User

# Create your models here.

TYPE=(
    ('New Order', 'Item Order'),
    ('Item Shipped', 'Item Shipped'),
    ('Item Delivered', 'Item Delivered'),
)

class Wishlist(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, related_name='wishlist')


    class Meta:
        verbose_name_plural='Wishlist'

    def __str__(self):
        if self.product.name:
            return self.product.name
        else:
            return 'Wishlist'

class Address(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name=models.CharField(max_length=200, null=True, blank=True, default=None)
    mobile=models.CharField(max_length=50, null=True, blank=True, default=None)
    email=models.CharField(max_length=100, null=True, blank=True, default=None)
    country=models.CharField(max_length=100, null=True, blank=True, default=None)
    state=models.CharField(max_length=100, default=None, blank=True, null=True)
    city = models.CharField(max_length=100, default=None, blank=True, null=True)
    address = models.CharField(max_length=100, default=None, blank=True, null=True)
    zip_code = models.CharField(max_length=100, default=None, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Customer Address'

    def __str__(self):
        return self.full_name

class Notifications(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    type=models.CharField(max_length=100, choices=TYPE, default=None)
    seen=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'Notification'

    def __str__(self):
        return self.type
