# Generated by Django 4.1.6 on 2023-02-25 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0007_alter_discountcode_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="address",
            field=models.TextField(blank=True, null=True),
        ),
    ]
