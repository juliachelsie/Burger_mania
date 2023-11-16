# Generated by Django 4.2.7 on 2023-11-16 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_remove_booking_booking_time_customer_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.IntegerField(default=None),
        ),
    ]
