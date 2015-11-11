# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import localflavor.us.models
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FishListing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nameOfFish', models.CharField(max_length=25)),
                ('fishPhoto', models.ImageField(blank=True, upload_to='', storage=django.core.files.storage.FileSystemStorage(location='/media/photos'))),
                ('fishDesc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('first_name', models.CharField(max_length=61)),
                ('last_name', models.CharField(max_length=61)),
                ('username', models.CharField(max_length=61)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=61)),
                ('zip_code', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('user_ptr', models.OneToOneField(serialize=False, to='buysell.User', auto_created=True, primary_key=True, parent_link=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_email_verified', models.BooleanField(default=False)),
            ],
            bases=('buysell.user',),
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('user_ptr', models.OneToOneField(serialize=False, to='buysell.User', auto_created=True, primary_key=True, parent_link=True)),
                ('street_address', models.CharField(max_length=100)),
                ('apartment_number', models.CharField(blank=True, max_length=10)),
                ('city', models.CharField(max_length=40)),
                ('state', localflavor.us.models.USStateField(max_length=2, choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')])),
                ('is_email_verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('bio', models.TextField(blank=True)),
                ('website', models.URLField()),
            ],
            bases=('buysell.user',),
        ),
        migrations.AddField(
            model_name='fishlisting',
            name='fishermanWomen',
            field=models.ForeignKey(to='buysell.Seller'),
        ),
    ]
