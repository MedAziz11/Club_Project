# Generated by Django 3.0.5 on 2020-04-13 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0009_auto_20200413_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='time',
        ),
        migrations.AlterField(
            model_name='request',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
