# Generated by Django 3.2 on 2022-12-06 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0006_auto_20221206_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='number',
            field=models.IntegerField(max_length=16, unique=True),
        ),
    ]
