# Generated by Django 3.1.4 on 2021-01-04 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floor',
            name='Number',
            field=models.CharField(max_length=1),
        ),
    ]