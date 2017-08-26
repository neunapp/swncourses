# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

#app curso
from applications.cursos.models import Course
# models
from .models import Banco, Registration

#registro desde admin
class RegistrationAdmin(admin.ModelAdmin):
    list_display = (
        'course',
        'user',
        'amount',
        'banco',
        'cod_transaction',
        'pk',
    )
    search_fields = ('user', 'cod_transaction')
    list_filter = ('course','user',)
    readonly_fields=('user',)
    fields = (
        'course',
        'user',
        'banco',
        'cod_transaction',
        'date_payment',
        'discount',
        'amount_discount',
        'activate',
        'anulate',
    )
    #
    list_filter = ('course__name',)
    raw_id_admin = ('course', )
    # def render_change_form(self, request, context, *args, **kwargs):
    #      context['adminform'].form.fields['course'].queryset = Course.objects.filter(name__iexact='company')
    #      return super(RegistrationAdmin, self).render_change_form(request, context, args, kwargs)


admin.site.register(Registration,RegistrationAdmin)
#
admin.site.register(Banco)
