from django.db import models

BRAND_CHOICES = [
	("Mercedes-Benz", "Mercedes-Benz"),
	("BMW", "BMW"),
	("Audi", "Audi"),
]


class Car(models.Model):
    brand = models.CharField(choices=BRAND_CHOICES, default='mercedes-benz', max_length=15, blank=False, null=False)
    model = models.CharField(max_length=20, blank=False, null=False)
    year = models.IntegerField(null=False, blank=False)
