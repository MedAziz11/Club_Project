# Generated by Django 3.0.5 on 2020-04-13 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0005_remove_request_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='time',
            field=models.TimeField(default=0),
        ),
        migrations.AlterField(
            model_name='request',
            name='date',
            field=models.DateField(),
        ),
    ]
