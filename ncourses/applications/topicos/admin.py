# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

#model
from .models import Topico, Video

class TopicoAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'minutes',
        'pk',
    )
    search_fields = ('name', 'description')

admin.site.register(Topico, TopicoAdmin)


class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'url_video',
        'minutes',
        'pk',
    )
    search_fields = ('url_video',)

admin.site.register(Video, VideoAdmin)
