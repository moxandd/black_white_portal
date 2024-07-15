from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.CharField(max_length=300, blank=True, null=True)
    price = models.FloatField(default=99.99)

    def __str__(self):
        return self.title