# Generated by Django 4.2 on 2023-05-10 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("seller", "0001_initial"),
        ("buyer", "0009_rename_is_paid_cartorder_is_check_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="seller_id",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="seller.seller",
            ),
        ),
    ]
