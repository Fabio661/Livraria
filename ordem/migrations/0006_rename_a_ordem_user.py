# Generated by Django 4.2 on 2023-04-28 00:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ordem", "0005_rename_user_ordem_a"),
    ]

    operations = [
        migrations.RenameField(
            model_name="ordem",
            old_name="a",
            new_name="user",
        ),
    ]
