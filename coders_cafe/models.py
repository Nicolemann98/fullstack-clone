from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    start_time = models.DateTimeField()
    num_seats = models.IntegerField()
    