# Generated by Django 2.0.7 on 2019-04-18 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0003_remove_donate_donate_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donate',
            name='amount',
            field=models.CharField(max_length=256),
        ),
    ]
