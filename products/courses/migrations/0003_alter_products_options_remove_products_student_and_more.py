# Generated by Django 5.0.2 on 2024-03-02 19:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0002_products_student_alter_products_author_teacher_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="products",
            options={"verbose_name": "Продукты", "verbose_name_plural": "Продукты"},
        ),
        migrations.RemoveField(
            model_name="products",
            name="student",
        ),
        migrations.AddField(
            model_name="group",
            name="student",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
