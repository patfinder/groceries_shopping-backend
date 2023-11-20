from django.db import models


class Product(models.Model):
    # id = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    created_time = models.DateTimeField()
    retailer = models.CharField(max_length=100)
    categories = models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    price = models.FloatField()
    old_price = models.FloatField()
    unit = models.CharField(max_length=20)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'created_time'], name='unique_name_created_time'
            )
        ]
