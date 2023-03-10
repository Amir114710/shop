# Generated by Django 4.1.6 on 2023-02-25 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0005_order_total_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="DiscountCode",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="نام کد تخفیف")),
                (
                    "discount",
                    models.SmallIntegerField(default=0, verbose_name="مقدار درصد تفیف"),
                ),
                (
                    "quantity",
                    models.SmallIntegerField(default=1, verbose_name="تعداد کد تخفیف"),
                ),
            ],
            options={
                "verbose_name": "کد تخفیف",
                "verbose_name_plural": "تنظیمات قسمت  کد های تخفیف",
            },
        ),
    ]
