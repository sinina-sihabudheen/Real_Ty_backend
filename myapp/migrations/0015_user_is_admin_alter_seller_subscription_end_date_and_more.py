# Generated by Django 5.0.6 on 2024-07-09 09:24

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_alter_seller_subscription_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='seller',
            name='subscription_end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 8, 8, 9, 24, 8, 85828, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]