# Generated by Django 4.2.1 on 2023-05-09 16:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buyer', '0005_remove_cart_is_paid_cartorder_is_paid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slip',
            name='product',
        ),
        migrations.AddField(
            model_name='slip',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
