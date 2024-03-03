# Generated by Django 5.0.2 on 2024-03-02 18:43

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="products",
            name="student",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="products",
            name="author_teacher",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="products",
            name="price",
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name="products",
            name="start_date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="products",
            name="start_time",
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="products",
            name="title",
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name="Group",
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
                ("group_title", models.CharField(db_index=True, max_length=100)),
                (
                    "prod",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="courses.products",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Lesson",
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
                ("lesson_title", models.CharField(db_index=True, max_length=100)),
                ("video_link", models.TextField()),
                (
                    "prod",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="courses.products",
                    ),
                ),
            ],
        ),
    ]
