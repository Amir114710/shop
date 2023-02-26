# Generated by Django 4.1.6 on 2023-02-20 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contactus", "0002_rename_contactus_contactusmodels"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contacts",
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
                    "address",
                    models.CharField(
                        blank=True,
                        max_length=1000,
                        null=True,
                        verbose_name="ادرس محل کار",
                    ),
                ),
                (
                    "phone_number",
                    models.BigIntegerField(
                        blank=True, null=True, verbose_name="تلفن محل کار"
                    ),
                ),
                (
                    "email_address",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        verbose_name="ایمیل محل کار",
                    ),
                ),
                (
                    "facebook",
                    models.CharField(
                        blank=True,
                        max_length=10000,
                        null=True,
                        verbose_name="ادرس فیس بوک",
                    ),
                ),
                (
                    "twiter",
                    models.CharField(
                        blank=True,
                        max_length=10000,
                        null=True,
                        verbose_name="ادرس تویتر",
                    ),
                ),
                (
                    "linkdin",
                    models.CharField(
                        blank=True,
                        max_length=10000,
                        null=True,
                        verbose_name="ادرس لینک دین",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "اطلاعات تماس",
                "verbose_name_plural": "تنظیمات قسمت اطلاعات تماس",
                "ordering": ("-created",),
            },
        ),
    ]
