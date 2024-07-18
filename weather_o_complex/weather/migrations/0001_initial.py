# Generated by Django 4.2.14 on 2024-07-17 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SearchHistory",
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
                ("city", models.CharField(max_length=80)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
