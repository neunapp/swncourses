# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

#models
from .models import Postulant, Suscription

class PostulantAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'phone',
        'contry',
        'city',
        'pk',
    )
    search_fields = ('full_name', 'email')
    list_filter = ('city','contry',)


admin.site.register(Postulant,PostulantAdmin)
admin.site.register(Suscription)
