from django import forms
from django.core import validators


from django.core.exceptions import ValidationError

__author__ = 'David'


class LoginForm(forms.Forms):
    first_name_form = forms.CharField(label="Your first name", max_length=61)
    last_name_form = forms.CharField(label="Last Name", max_length=61)
    email_form = forms.EmailField(label="Email", validators=[validators.EmailValidator])


class RegistrationForm(forms.Form):
    first_name_form = forms.CharField(label="First name", max_length=61)
    last_name_form = forms.CharField(label="Last Name", max_length=61)
    email_form = forms.EmailField(label="Email", validators=[validators.EmailValidator])


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
    phish_photo = forms.FileField()
    fish_description = forms.Textarea()
