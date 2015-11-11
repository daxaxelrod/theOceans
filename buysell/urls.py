from django.conf.urls import include, url
from django.contrib import admin
from . import views

__author__ = 'David'
""" Buysell URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""


urlpatterns = [
    url(r'login/', views.login(), name="login"),
    url(r'register-buyer/', views.registration_buyer(), name="buyerReg"),
    # url(r'^fishbuy/' , include(views.hello_fishy)),


]