# Generated by Django 3.0.5 on 2020-04-13 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='statu',
            field=models.CharField(choices=[('await', 'Await'), ('process', 'Accepted'), ('denied', 'Denied')], default='await', max_length=10),
        ),
    ]
