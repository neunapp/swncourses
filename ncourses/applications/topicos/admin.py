# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

#model
from .models import Topico

class TopicoAdmin(admin.ModelAdmin):
    list_display = (
        'course',
        'name',
        'url_video',
        'minutes',
        'pk',
    )
    search_fields = ('name', 'description')
    list_filter = ('course',)

admin.site.register(Topico, TopicoAdmin)
