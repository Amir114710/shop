# Generated by Django 4.1.6 on 2023-02-26 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("shop", "0012_notification"),
    ]

    operations = [
        migrations.CreateModel(
            name="NotificationPersonal",
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
                ("content", models.TextField(verbose_name="متن اعلان")),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="notification_personal",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="انتخاب کاربر",
                    ),
                ),
            ],
            options={
                "verbose_name": "اعلان",
                "verbose_name_plural": "اعلان ها",
                "ordering": ("-created",),
            },
        ),
    ]
