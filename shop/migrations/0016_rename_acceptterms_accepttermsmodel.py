# Generated by Django 4.1.5 on 2023-03-10 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0015_acceptterms_alter_comments_message_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="AcceptTerms",
            new_name="AcceptTermsModel",
        ),
    ]
