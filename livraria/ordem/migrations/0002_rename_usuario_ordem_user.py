# Generated by Django 4.2 on 2023-04-28 00:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ordem", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="ordem",
            old_name="usuario",
            new_name="user",
        ),
    ]
