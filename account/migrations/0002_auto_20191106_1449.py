# Generated by Django 2.2.7 on 2019-11-06 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phonenumber',
            field=models.IntegerField(unique=True, verbose_name='شماره تماس'),
        ),
    ]
