# Generated by Django 3.0.5 on 2020-04-13 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0008_auto_20200413_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='date',
            field=models.DateField(),
        ),
    ]