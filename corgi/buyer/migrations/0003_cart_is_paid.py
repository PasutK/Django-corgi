# Generated by Django 4.2 on 2023-05-08 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
