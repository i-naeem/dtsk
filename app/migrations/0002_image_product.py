# Generated by Django 5.0.7 on 2024-07-11 11:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="image",
            name="product",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="app.product"
            ),
            preserve_default=False,
        ),
    ]
