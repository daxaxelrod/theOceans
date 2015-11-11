from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from .forms import *
from .models import *

# Create your views here.

# TODO check work here. Unexperienced in middleware. resourcees onlince
# def process_request(self, request):
#     request.DATABASE.connect()
#     return

def send_welcome_email(subject, message, sender, new_user):
    from django.core.mail import send_mail
    send_mail(subject, message,sender, new_user)
    return



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
    return render(request, "upload_fish_listing.html")

def registration_buyer(request):
    form = RegistrationBuyerExten(request.POST)
    if form.is_valid():
        new_user = Buyer.create(
            # new user time boooiiii
            first_name = form.first_name_form,
            last_name=form.last_name_form,
            email=form.email_form,
            # pass
            zip_code=form.zip_code_form
        )
    else:
        return HttpResponse("We had trouble processing your form. Can you try again")





        # abstract this to a test one day but as long as it works here that is fine
      #  authenticate_user_and_login = authenticate(username=)

    return render(request, "register.html")




