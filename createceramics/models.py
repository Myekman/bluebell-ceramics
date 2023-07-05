from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

SERVICE_CHOICES = (
    ("Paint", "Paint"),
    ("Turn", "Turn"),
    )

TIME_CHOICES = (
    ("9:00", "9:00"),
    ("10:00", "10:00"),
    ("11:00", "11:00"),
    ("12:00", "12:00"),
    ("13:00", "13:00"),
    ("14:00", "14:00"),
    ("15:00", "15:00"),
    ("16:00", "16:00"),
    ("17:00", "17:00"),
    ("18:00", "18:00"),
)

GUESTS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
)


class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_booking")
    email = models.EmailField()
    phone = models.IntegerField(blank=True, null=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="Paint")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="12:00")
   
    

    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"
