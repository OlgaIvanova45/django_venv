from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Products(models.Model):
    author_teacher = models.CharField(max_length=255, verbose_name='Автор/Преподаватель')
    title = models.CharField(max_length=255, verbose_name='Название')
    # student = models.ForeignKey(User, on_delete=models.PROTECT, default=None)
    start_date = models.DateField(verbose_name='Дата начала')
    start_time = models.TimeField(default=timezone.now, verbose_name='Время начала')
    price = models.FloatField(verbose_name='Цена')


    def set_group_size(self, min_people, max_people):
        self.min_people = min_people
        self.max_people = max_people


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'


# class Student(models.Model):
#     name = models.CharField(max_length=30)
#     products = models.ManyToManyField(Products)


class Group(models.Model):
    student = models.ForeignKey(User, on_delete=models.PROTECT, default=None, verbose_name='Имя студента')
    group_title = models.CharField(max_length=100, db_index=True, verbose_name='Название группы')
    prod = models.ForeignKey('Products', on_delete=models.PROTECT, verbose_name='Продукт')


    def __str__(self):
        return self.group_title


    class Meta:
        ordering = ('group_title',)
        verbose_name = 'Группы'
        verbose_name_plural = 'Группы'


class Lesson(models.Model):
    lesson_title = models.CharField(max_length=100, db_index=True, verbose_name='Название урока')
    video_link = models.URLField(verbose_name='Ссылка на видео')
    prod = models.ForeignKey('Products', on_delete=models.PROTECT, verbose_name='Продукт')

    def __str__(self):
        return self.lesson_title

    class Meta:
        ordering = ('lesson_title',)
        verbose_name = 'Уроки'
        verbose_name_plural = 'Уроки'
