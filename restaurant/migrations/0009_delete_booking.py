# Generated by Django 4.2.7 on 2023-11-22 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_remove_table_restaurant_delete_restaurant_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
