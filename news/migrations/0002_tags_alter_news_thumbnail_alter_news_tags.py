# Generated by Django 5.0.7 on 2024-09-29 10:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="tags",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name="news",
            name="thumbnail",
            field=models.ImageField(blank=True, null=True, upload_to="news_thumbnail/"),
        ),
        migrations.AlterField(
            model_name="news",
            name="tags",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="news.tags"
            ),
        ),
    ]
