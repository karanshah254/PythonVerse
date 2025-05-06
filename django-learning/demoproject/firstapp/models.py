from django.db import models


# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()


class Reservation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    guestCount = models.IntegerField()
    reservationTime = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)
