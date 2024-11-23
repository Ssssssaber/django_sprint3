# Generated by Django 5.0.3 on 2024-11-23 08:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "категория", "verbose_name_plural": "Категории"},
        ),
        migrations.AlterModelOptions(
            name="location",
            options={
                "verbose_name": "местоположение",
                "verbose_name_plural": "Местоположения",
            },
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"verbose_name": "публикация", "verbose_name_plural": "Публикации"},
        ),
        migrations.AddField(
            model_name="category",
            name="created_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Добавлено"),
        ),
        migrations.AddField(
            model_name="category",
            name="is_published",
            field=models.BooleanField(
                default=True,
                help_text="Снимите галочку, чтобы скрыть публикацию.",
                verbose_name="Опубликовано",
            ),
        ),
        migrations.AddField(
            model_name="location",
            name="created_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Добавлено"),
        ),
        migrations.AddField(
            model_name="location",
            name="is_published",
            field=models.BooleanField(
                default=True,
                help_text="Снимите галочку, чтобы скрыть публикацию.",
                verbose_name="Опубликовано",
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="created_at",
            field=models.DateTimeField(auto_now=True, verbose_name="Добавлено"),
        ),
        migrations.AddField(
            model_name="post",
            name="is_published",
            field=models.BooleanField(
                default=True,
                help_text="Снимите галочку, чтобы скрыть публикацию.",
                verbose_name="Опубликовано",
            ),
        ),
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(
                help_text="Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.",
                unique=True,
                verbose_name="Идентификатор",
            ),
        ),
        migrations.AlterField(
            model_name="location",
            name="name",
            field=models.CharField(max_length=256, verbose_name="Название места"),
        ),
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Автор публикации",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="location",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="blog.location",
                verbose_name="Местоположение",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="pub_date",
            field=models.DateTimeField(
                help_text="Если установить дату и время в будущем — можно делать отложенные публикации.",
                verbose_name="Дата и время публикации",
            ),
        ),
    ]