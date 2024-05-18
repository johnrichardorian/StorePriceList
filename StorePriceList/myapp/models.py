from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.

class StoreProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    store_name = models.CharField('Store Name', max_length=100)
    address = models.CharField(max_length=100)
    zip_code = models.CharField('Zip Code', max_length=15)
    phone = models.CharField('Phone', max_length=25)
    email_address = models.EmailField('Email Address')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.store_name
    

class Inventory(models.Model):
    product_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    store_profile = models.ForeignKey(StoreProfile, blank=True, null=True, on_delete=models.CASCADE)
    product_name = models.CharField('Product Name', max_length=100)  
    product_description = models.TextField(blank=True)
    price = models.DecimalField('Price', max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name