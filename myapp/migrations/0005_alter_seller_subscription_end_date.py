# Generated by Django 5.0.6 on 2024-06-27 13:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_seller_subscription_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='subscription_end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 27, 13, 0, 53, 875036, tzinfo=datetime.timezone.utc)),
        ),
    ]
