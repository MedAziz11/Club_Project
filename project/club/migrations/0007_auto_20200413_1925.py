# Generated by Django 3.0.5 on 2020-04-13 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0006_auto_20200413_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='time',
            field=models.TimeField(blank=True),
        ),
    ]