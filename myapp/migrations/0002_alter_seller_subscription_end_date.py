# Generated by Django 5.0.6 on 2024-06-24 05:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='subscription_end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 24, 5, 59, 39, 677296, tzinfo=datetime.timezone.utc)),
        ),
    ]
