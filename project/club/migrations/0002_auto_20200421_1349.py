# Generated by Django 3.0.5 on 2020-04-21 13:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 21, 13, 49, 13, 869716)),
        ),
    ]
