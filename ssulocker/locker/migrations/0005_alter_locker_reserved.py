# Generated by Django 3.2.9 on 2021-11-15 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locker', '0004_alter_personalinfo_lockernum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locker',
            name='reserved',
            field=models.IntegerField(default=0),
        ),
    ]