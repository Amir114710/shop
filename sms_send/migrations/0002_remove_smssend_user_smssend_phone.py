# Generated by Django 4.1.5 on 2023-03-11 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sms_send", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="smssend",
            name="user",
        ),
        migrations.AddField(
            model_name="smssend",
            name="phone",
            field=models.IntegerField(blank=True, null=True, verbose_name="کاربر"),
        ),
    ]
