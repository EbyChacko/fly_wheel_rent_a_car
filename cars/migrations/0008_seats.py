# Generated by Django 5.0.4 on 2024-04-22 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_alter_booking_county_alter_personaldetails_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats', models.IntegerField()),
            ],
            options={
                'ordering': ['seats'],
            },
        ),
    ]
