# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# models
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'video',
        'image',
        'image_url',
        'teacher',
        'state',
        'point',
        'visit',
        'pk',
    )
    search_fields = ('name', 'description_short')
    list_filter = ('category','price',)
    fields = (
        'name',
        'category',
        'price',
        'video',
        'image',
        'image_url',
        'description_short',
        'description_large',
        'resume',
        'recomendation',
        'teacher',
        'nivel',
        'tags',
        'state',
    )
    filter_horizontal = ('tags',)


admin.site.register(Course,CourseAdmin)
