# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# models

from .models import Category, Recomendation, Tag


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'pk',
    )
    search_fields = ('name', 'description')

admin.site.register(Category, CategoryAdmin)


class RecomendationAdmin(admin.ModelAdmin):
    list_display = (
        'description',
        'pk',
    )
    search_fields = ('description',)

admin.site.register(Recomendation, RecomendationAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'pk',
    )
    search_fields = ('name',)

admin.site.register(Tag)
