from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    date = models.DateField()
    start_time = models.IntegerField(validators=[MinValueValidator(8), MaxValueValidator(19)])
    num_seats = models.IntegerField()
    