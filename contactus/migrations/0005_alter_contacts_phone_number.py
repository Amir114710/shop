# Generated by Django 4.1.6 on 2023-02-20 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contactus", "0004_alter_contacts_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contacts",
            name="phone_number",
            field=models.BigIntegerField(
                blank=True, null=True, verbose_name="تلفن محل کار"
            ),
        ),
    ]