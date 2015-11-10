from django.db import models
import os
import datetime
from django.core.files.storage import FileSystemStorage
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.models import USStateField
from slugify import slugify


# Create your models here.

# class User(models.User):
#     username = CharField(max255)

fs = FileSystemStorage(location="/media/photos")


class User(models.Model):
    first_name = models.CharField(max_length=61)
    last_name = models.CharField(max_length=61)
    email = models.EmailField()
    password = models.PasswordField()
    zip_code = models.CharField(max_length=255, blank=True)


class Buyer(User):
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    is_authenticated = models.BooleanField(default=False)
    # only possible blank page
    # seller needs location info
    # They need to link a credit card


class Seller(User):
    street_address = models.CharField(max_length=100)
    apartment_number = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=40)
    state = USStateField(choices=STATE_CHOICES)
    is_authenticated = models.BooleanField(default=False)
    # fishProducts = models.
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    bio = models.TextField(blank=True)
    website = models.URLField()

    def _get_full_name(self):
        """Returns the person's full name."""
        return '%s %s' % (self.first_name, self.last_name)
    full_name = property(_get_full_name)


class FishListing(models.Model):
    nameOfFish = models.CharField(max_length=25)
    # this way or
    # photosOfProduct = models.ImageField(storage=fs, blank=True)
    # this way

    @staticmethod
    def generate_upload_path(filename):
        filename, ext = os.path.splitext(filename.lower())
        filename = "%s.%s%s" % (slugify(filename), datetime.datetime.now().strftime("%Y-%m-%d.%H-%M-%S"), ext)
        return '%s%s' % (fs, filename)
    fishPhoto = models.ImageField(blank=True, upload_to=generate_upload_path)

    # many to one to seller relationship
    fishermanWomen = models.ForeignKey(Seller)
    fishDesc = models.TextField()

#
# Chet Faker featuring banks
