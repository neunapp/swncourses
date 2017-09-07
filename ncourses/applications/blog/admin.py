# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Blog, BlogCategory, Commentary, Tag

#
class BlogAdmin(admin.ModelAdmin):
   list_display = (
       'title',
       'author',
       'published',
       'score',
       'created_by',
       'category',
       'created'
   )
   search_fields = ('title',)
   list_filter = ('category','published','author',)
   fields =(
        'title',
        'description',
        'content',
        'category',
        'image',
        'tag',
        'published',
        'author',
        'created_by',
   )
   filter_horizontal = ('tag',)


admin.site.register(Blog, BlogAdmin )
admin.site.register(BlogCategory)
admin.site.register(Commentary)
admin.site.register(Tag)
