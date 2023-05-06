# Generated by Django 4.2 on 2023-05-06 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("buyer", "0001_initial"),
        ("seller", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
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
        ),
    ]
