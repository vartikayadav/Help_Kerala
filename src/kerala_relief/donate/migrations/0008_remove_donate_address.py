# Generated by Django 2.0.7 on 2019-04-19 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0007_auto_20190419_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donate',
            name='address',
        ),
    ]
