# Generated by Django 4.2 on 2023-04-28 00:39

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ordem", "0003_rename_user_ordem_user_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="ordem",
            old_name="user_id",
            new_name="user",
        ),
    ]
