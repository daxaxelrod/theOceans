from django.db import models

# Create your models here.

# class User(models.User):
#     username = CharField(max255)

class Buyer(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

class Seller(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

#
# Chet Faker featuring banks
