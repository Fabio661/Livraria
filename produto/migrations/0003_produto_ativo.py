# Generated by Django 4.2 on 2023-04-28 04:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("produto", "0002_remove_produto_ativo"),
    ]

    operations = [
        migrations.AddField(
            model_name="produto",
            name="ativo",
            field=models.BooleanField(default=True),
        ),
    ]