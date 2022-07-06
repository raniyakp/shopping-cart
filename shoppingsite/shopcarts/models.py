from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.forms import ModelForm

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, null=True, upload_to = 'dp/')
    phone = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True,null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    pincode = models.DecimalField(max_digits=6,decimal_places=0, blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name()

class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(blank=True, null=True)
    parent = models.ForeignKey('self', on_delete= models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    items= models.ManyToManyField(Product,through='CartItem')

    def __str__(self):
        return self.user.first_name


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,blank=True,null=True)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.product.name

   
class Order(models.Model):
    items = models.ManyToManyField(Product, through='ProductOrder')
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = (
        ("na","None"),
        ("Cancelled","Cancelled"),
        ("Ordered","Ordered"),
        ("Shipped","Shipped"),
        ("Delivered","Delivered"),
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="None")
    updated_at = models.DateTimeField(auto_now=True)
    shippingaddress = models.TextField(blank=True, null=True)

class ProductOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)








    





    

