from django.db import models
from django.core.files.storage import FileSystemStorage
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.models import USStateField
# Create your models here.

# class User(models.User):
#     username = CharField(max255)

fs = FileSystemStorage(location="/media/photos")

class Buyer(models.Model):
    first_name = models.CharField(max_length=61)
    last_name = models.CharField(max_length=61)
    email = models.EmailsField()
    password = models.PasswordField()
    location = models.CharField(max_length=255)
    created_at = models.DateTime()
    is_authenticated = models.BooleanField(default=False)


# seller needs location info
# They need to link a credit card


class Seller(models.Model):
    first_name = models.CharField(max_length=61)
    last_name = models.CharField(max_length=61)
    street_address = models.CharField(max_length=100)
    apartment_number = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=40)
    state = USStateField(choices=STATE_CHOICES)
    is_authenticated = models.BooleanField(default=False)
    # fishProducts = models.

    def _get_full_name(self):
        """Returns the person's full name."""
        return '%s %s' % (self.first_name, self.last_name)
    full_name = property(_get_full_name)



class FishListing(models.Model):
    nameOfFish = models.CharField(max_length=25)
    photosOfProduct = models.ImageField(storage=fs)
    # many to one to seller relationship
    fishermanWomen = models.ForeignKey(Seller)

#
# Chet Faker featuring banks
