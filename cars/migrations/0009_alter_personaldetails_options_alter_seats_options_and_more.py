# Generated by Django 5.0.4 on 2024-04-29 12:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_seats'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personaldetails',
            options={'ordering': ['name'], 'verbose_name_plural': 'Personal Details'},
        ),
        migrations.AlterModelOptions(
            name='seats',
            options={'ordering': ['seats'], 'verbose_name_plural': 'Seats'},
        ),
        migrations.AlterField(
            model_name='car',
            name='seats',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.seats'),
        ),
    ]
