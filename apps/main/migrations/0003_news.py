# Generated by Django 5.1.4 on 2024-12-28 13:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_settings_all"),
    ]

    operations = [
        migrations.CreateModel(
            name="News",
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
                ("image", models.ImageField(upload_to="news", verbose_name="Фото")),
                ("title", models.CharField(max_length=155, verbose_name="Заголовок")),
                (
                    "title2",
                    models.CharField(max_length=155, verbose_name="Заголовок 2"),
                ),
                (
                    "title3",
                    models.CharField(max_length=155, verbose_name="Заголовок 3"),
                ),
                ("text1", models.TextField(verbose_name="Описание 1")),
                ("text2", models.TextField(verbose_name="Описание 2")),
                ("image2", models.ImageField(upload_to="news", verbose_name="Фото 2")),
                (
                    "title4",
                    models.CharField(max_length=155, verbose_name="Заголовок 4"),
                ),
                (
                    "title5",
                    models.CharField(max_length=155, verbose_name="Заголовок 5"),
                ),
                (
                    "title6",
                    models.CharField(max_length=155, verbose_name="Заголовок 6"),
                ),
                ("text3", models.TextField(verbose_name="Описание 3")),
                ("text4", models.TextField(verbose_name="Описание 4")),
            ],
            options={
                "verbose_name_plural": "Новости",
            },
        ),
    ]
