# Generated by Django 4.2 on 2023-05-03 16:40

from django.db import migrations, models
import django.db.models.deletion
import seller.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, validators=[seller.models.validate_buyer_email])),
                ('password', models.CharField(max_length=100)),
                ('store_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12, validators=[seller.models.validate_buyer_phone])),
                ('address', models.CharField(max_length=300)),
                ('store_image', models.ImageField(upload_to='seller/media/store/')),
                ('qrcode_image', models.ImageField(upload_to='seller/media/qrcode/')),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SellerCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='seller/media/category')),
            ],
        ),
        migrations.CreateModel(
            name='SellerProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('description', models.CharField(max_length=2500)),
                ('image', models.ImageField(upload_to='seller/media/product')),
                ('status', models.BooleanField(default=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='seller.sellercategory')),
                ('seller', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='seller.seller')),
            ],
        ),
    ]