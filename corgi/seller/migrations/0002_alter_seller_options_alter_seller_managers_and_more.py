# Generated by Django 4.2 on 2023-05-06 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("seller", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="seller",
            options={},
        ),
        migrations.AlterModelManagers(
            name="seller",
            managers=[],
        ),
        migrations.RemoveField(
            model_name="seller",
            name="email",
        ),
        migrations.RemoveField(
            model_name="seller",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="seller",
            name="groups",
        ),
        migrations.RemoveField(
            model_name="seller",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="seller",
            name="is_staff",
        ),
        migrations.RemoveField(
            model_name="seller",
            name="is_superuser",
        ),
        migrations.RemoveField(
            model_name="seller",
            name="last_login",
        ),
        migrations.RemoveField(
            model_name="seller",
            name="last_name",
        ),
        migrations.RemoveField(
            model_name="seller",
            name="password",
        ),
        migrations.RemoveField(
            model_name="seller",
            name="user_permissions",
        ),
        migrations.RemoveField(
            model_name="seller",
            name="username",
        ),
        migrations.AlterField(
            model_name="sellerproduct",
            name="seller",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="seller.seller"
            ),
        ),
    ]
