# Generated by Django 2.0.7 on 2019-04-17 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donors', models.CharField(max_length=256)),
                ('raised', models.CharField(max_length=256)),
                ('exp', models.CharField(max_length=256)),
                ('countries', models.CharField(max_length=256)),
            ],
        ),
    ]
