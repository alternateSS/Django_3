# Generated by Django 3.2 on 2022-12-06 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0003_auto_20221206_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='credit.client'),
        ),
    ]