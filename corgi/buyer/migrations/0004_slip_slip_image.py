# Generated by Django 4.2.1 on 2023-05-09 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0003_slip'),
    ]

    operations = [
        migrations.AddField(
            model_name='slip',
            name='slip_image',
            field=models.ImageField(default=1, upload_to='buyer/media/slip/'),
            preserve_default=False,
        ),
    ]