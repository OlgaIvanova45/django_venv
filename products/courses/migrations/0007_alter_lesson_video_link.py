# Generated by Django 5.0.2 on 2024-03-02 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0006_alter_lesson_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="video_link",
            field=models.FilePathField(path="/videos", verbose_name="Ссылка на видео"),
        ),
    ]
