# Generated by Django 5.0.4 on 2024-04-17 20:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_categories_alter_car_city_alter_car_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ['fuel'],
            },
        ),
        migrations.AlterField(
            model_name='car',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.categories'),
        ),
        migrations.AlterField(
            model_name='car',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.cities'),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.fuel'),
        ),
    ]
