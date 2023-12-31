# Generated by Django 4.2.7 on 2023-11-16 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_time',
        ),
        migrations.AddField(
            model_name='customer',
            name='first_name',
            field=models.CharField(default=False, max_length=200),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_name',
            field=models.CharField(default=False, max_length=200),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.IntegerField(default=False),
        ),
    ]
