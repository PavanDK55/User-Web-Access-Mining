# Generated by Django 2.2.8 on 2020-01-14 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
