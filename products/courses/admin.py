from django.contrib import admin

# Register your models here.
from .models import *


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_teacher', 'title', 'start_date', 'start_time', 'price')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'author_teacher')


class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson_title', 'video_link', 'prod')
    list_display_links = ('id', 'lesson_title')
    search_fields = ('lesson_title', 'prod')


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'group_title', 'prod')
    list_display_links = ('id', 'group_title')
    search_fields = ('group_title', 'student')


admin.site.register(Products, ProductsAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Group, GroupAdmin)
