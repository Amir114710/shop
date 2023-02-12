# Generated by Django 4.1.6 on 2023-02-12 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                (
                    "image",
                    models.FileField(
                        upload_to="shop/category", verbose_name="عکس دسته بندی"
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        max_length=150,
                        null=True,
                        verbose_name="نام دسته بندی",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "دسته بندی",
                "verbose_name_plural": "تنظیمات قسمت دسته بندی",
            },
        ),
        migrations.CreateModel(
            name="Tags",
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
                (
                    "title",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="نام برچسب"
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "برچسب",
                "verbose_name_plural": "تنظیمات قسمت  برچسب ها",
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                (
                    "title",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="نام کالا"
                    ),
                ),
                (
                    "discription",
                    models.TextField(
                        blank=True, null=True, verbose_name="توضیحات کوتاه"
                    ),
                ),
                (
                    "price",
                    models.SmallIntegerField(
                        blank=True, null=True, verbose_name="قیمت کالا"
                    ),
                ),
                (
                    "code",
                    models.SmallIntegerField(
                        blank=True, null=True, unique=True, verbose_name="کد کالا"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="shop/products", verbose_name="عکس کالا"
                    ),
                ),
                (
                    "status",
                    models.BooleanField(default=True, verbose_name="ایا موجود است ؟"),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "category",
                    models.ManyToManyField(
                        blank=True,
                        null=True,
                        to="shop.category",
                        verbose_name="دسته بندی محصول",
                    ),
                ),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True, null=True, to="shop.tags", verbose_name="برچسب"
                    ),
                ),
            ],
            options={
                "verbose_name": "محصولات",
                "verbose_name_plural": "تنظیمات قسمت محصولات",
            },
        ),
    ]