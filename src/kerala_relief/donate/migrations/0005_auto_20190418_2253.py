# Generated by Django 2.0.7 on 2019-04-18 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0004_auto_20190418_2233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donate',
            old_name='amount',
            new_name='total',
        ),
    ]
