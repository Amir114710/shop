# Generated by Django 4.1.6 on 2023-02-27 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0013_notificationpersonal"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="notificationpersonal",
            options={
                "ordering": ("-created",),
                "verbose_name": "اعلان",
                "verbose_name_plural": "اعلان های شخصی کاربران",
            },
        ),
    ]