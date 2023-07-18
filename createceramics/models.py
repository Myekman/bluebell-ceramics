from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


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
        User, on_delete=models.CASCADE, related_name="user_booking", blank=True, null=True)
    name = models.CharField(max_length=70, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES, default="Paint")
    guests = models.CharField(max_length=2, choices=GUESTS, default='2')
    date = models.DateField(default=datetime.now, blank=True)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="12:00")

    class Meta:
        unique_together = ['user', 'date', 'time', 'service']

    def validate_unique(self, *args, **kwargs):
        super().validate_unique(*args, **kwargs)

        if Booking.objects.filter(user=self.user, date=self.date, time=self.time, service=self.service).exists():
            raise ValidationError('please pick another time')

    def __str__(self):
        return self.name
