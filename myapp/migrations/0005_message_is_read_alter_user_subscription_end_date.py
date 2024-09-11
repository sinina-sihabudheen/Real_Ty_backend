# Generated by Django 5.0.6 on 2024-09-05 03:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_user_subscription_end_date_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='subscription_end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 5, 3, 57, 0, 633305, tzinfo=datetime.timezone.utc)),
        ),
    ]
