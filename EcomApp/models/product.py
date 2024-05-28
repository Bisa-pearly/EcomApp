from django.db import models


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=2, unique=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
