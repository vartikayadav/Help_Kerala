# Generated by Django 2.0.7 on 2019-04-07 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalcare', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='city',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
