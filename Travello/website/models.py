from django.db import models


class Destination(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    covid = models.BooleanField(default=True)
    offer = models.BooleanField(default=False)


# Create your models here.
