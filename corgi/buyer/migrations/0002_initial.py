<<<<<<< HEAD
# Generated by Django 4.2 on 2023-05-06 03:04
=======
# Generated by Django 4.2 on 2023-05-05 18:16
>>>>>>> 621f7259bef01371b6e97090b84aea1e8aee9a5f

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        ('seller', '0001_initial'),
        ('buyer', '0001_initial'),
=======
        ("seller", "0001_initial"),
        ("buyer", "0001_initial"),
>>>>>>> 621f7259bef01371b6e97090b84aea1e8aee9a5f
    ]

    operations = [
        migrations.AddField(
<<<<<<< HEAD
            model_name='product',
            name='seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='seller.seller'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.buyerprofile'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.product'),
=======
            model_name="product",
            name="seller",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="seller.seller",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="buyer.buyerprofile"
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="buyer.product"
            ),
>>>>>>> 621f7259bef01371b6e97090b84aea1e8aee9a5f
        ),
    ]
