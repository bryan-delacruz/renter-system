# Generated by Django 3.1.4 on 2021-01-04 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_floor_buildingid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floor',
            name='buildingId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.building'),
        ),
    ]
