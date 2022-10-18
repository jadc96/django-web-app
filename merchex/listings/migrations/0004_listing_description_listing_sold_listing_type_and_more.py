# Generated by Django 4.1.2 on 2022-10-17 13:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_band_active_band_biography_band_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='listing',
            name='type',
            field=models.CharField(choices=[('R', 'Records'), ('P', 'Posters'), ('C', 'Clothings'), ('M', 'Miscellaneous')], default='R', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='year',
            field=models.IntegerField(default=1980, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2021)]),
            preserve_default=False,
        ),
    ]
