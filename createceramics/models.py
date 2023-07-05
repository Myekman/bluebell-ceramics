from django.db import models


# Create your models here.

# class Service(models.Model):
#     """The model is used to display data about the services
#     provided by the barbershop
#     """
#     service_name = models.CharField(max_length=150, unique=True)
#     price = models.DecimalField(max_digits=5, decimal_places=2)

#     class Meta:
#         unique_together = ('service_name', 'price', )
#         ordering = ['-price']

#     def __str__(self):
#         return f"{self.service_name}, {self.price}"

