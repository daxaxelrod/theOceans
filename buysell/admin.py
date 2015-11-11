from django.contrib import admin
from .models import Buyer
from .models import Seller
from .models import FishListing
from django import forms


# Register your models here.

admin.site.register([Buyer, Seller, FishListing])
