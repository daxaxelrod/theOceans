from django.shortcuts import render

from .forms import *
from .models import *

# Create your views here.

# TODO check work here. Unexperienced in middleware. resourcees onlince
# def process_request(self, request):
#     request.DATABASE.connect()
#     return

def upload_fish_listing(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            form = NewFishForVendor(request.POST, request.FILES)
            if form.is_valid():
                models.FishListing.create(
                    # could be dangerous if this doesn't work how i think it does
                    nameOfFish=form.fish_name,
                    fishPhoto=form.phish_photo,
                    fishDesc=form.fish_description,
                    fishermanWomen=request.user
                )
                return render(request, "index.html")
    else:
        return render(request, "Hey! you haave to login or register first")


def registration_buyer(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        new_user = Buyer.create(
            # new user time boooiiii

        )

    return render(request, "register.html")




