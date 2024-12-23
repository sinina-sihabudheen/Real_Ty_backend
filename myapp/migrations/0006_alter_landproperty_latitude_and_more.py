# Generated by Django 5.0.6 on 2024-09-12 13:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_message_is_read_alter_user_subscription_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landproperty',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='landproperty',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='residentialproperty',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='residentialproperty',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='subscription_end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 12, 13, 30, 21, 668681, tzinfo=datetime.timezone.utc)),
        ),
    ]
