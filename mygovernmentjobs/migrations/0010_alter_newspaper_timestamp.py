# Generated by Django 3.2.5 on 2021-09-06 12:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mygovernmentjobs', '0009_newspaper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspaper',
            name='timestamp',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]