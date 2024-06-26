# Generated by Django 5.0.4 on 2024-04-17 21:40

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_title_alter_booking_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='county',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='personaldetails',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
