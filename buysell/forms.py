from django import forms
from django.core import validators


from django.core.exceptions import ValidationError

__author__ = 'David'


def name_exists(form, field):
    # does the user exist in the data base
    if False: # check the user and see if it exists
        raise ValidationError("You need to pick a different username")
    else:
        return


def usernameExists(form, field):
    form.data

class LoginForm(forms.Forms):
    first_name_form = forms.CharField(label="Your first name", max_length=61)
    last_name_form = forms.CharField(label="Last Name", max_length=61)
    email_form = forms.EmailField(label="Email", validators=[validators.EmailValidator])


class RegistrationForm(forms.Form):                                                         #method or prop
    username_form = forms.CharField(label="Enter desired username", max_length=61,validators=[usernameExists])
    first_name_form = forms.CharField(label="First name", max_length=61, validators=[name_exists()])
    last_name_form = forms.CharField(label="Last Name", max_length=61)
    password_form = forms.CharField(label="Enter Password" ,widget=forms.PasswordInput())
    password_confirm_form = forms.CharField("Please Ccnfirm Your Password", widget=forms.PasswordInput)
    email_form = forms.EmailField(label="Email", validators=[validators.EmailValidator])



class RegistrationBuyerExten(RegistrationForm):
    zip_code_form = forms.IntegerField(label="Whats your zip code?", min_value=5)


class ContactForm(forms.Form):
    name_form = forms.CharField(label="Name", max_length=122)
    email = forms.CharField(label="Email", max_length=122, validators=[validators.EmailValidator])

VALID_IMAGE_EXTENSIONS = [
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
]


class NewFishForVendor(forms.Form):
    fish_name = forms.CharField(label="Name of Fish", max_length=40, validators=[validators.MinLengthValidator()])
    phish_photo = forms.FileField()  # this works well
    fish_description = forms.Textarea()
