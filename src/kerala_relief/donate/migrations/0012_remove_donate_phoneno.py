# Generated by Django 2.0.7 on 2019-04-19 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0011_auto_20190419_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donate',
            name='phoneno',
        ),
    ]
