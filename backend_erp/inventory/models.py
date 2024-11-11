from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField  # Chỉ sử dụng với PostgreSQL

class Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    category = ArrayField(models.CharField(max_length=100), blank=True, null=True)
    image = ArrayField(models.URLField(max_length=200), blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    unitcount = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    expiredate = models.DateField(_("Expiry Date"))
    isAvailable = models.BooleanField(_("Is Available"), default=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=255)
    materials = models.ManyToManyField(Material, related_name="products")
    sellingPrice = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = ArrayField(models.URLField(max_length=200), blank=True, null=True)
    expiredate = models.DateField(_("Expiry Date"))
    isAvailable = models.BooleanField(_("Is Available"), default=True)

    def __str__(self):
        return self.name