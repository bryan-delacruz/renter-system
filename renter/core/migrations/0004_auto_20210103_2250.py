# Generated by Django 3.1.4 on 2021-01-04 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_room_pricemaintenance'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='priceWarranty',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]