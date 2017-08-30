# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

#app curso
from applications.cursos.models import Course
# models
from .models import Banco, Registration


#registro desde admin
#personalizamos la columna course
def course(obj):
    return obj.course.name
course.short_description = 'Curso'

#personalizamos la columna user
def user(obj):
    return obj.user.email
user.short_description = 'Alumno'

class RegistrationAdmin(admin.ModelAdmin):
    list_display = (
        course,
        user,
        'amount',
        'banco',
        'cod_transaction',
        'activate',
        'pk',
    )
    course.short_description = 'Curso'
    search_fields = ('user', 'cod_transaction')
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
    list_filter = ('course__name','activate','created')
    raw_id_admin = ('course', )
    # def render_change_form(self, request, context, *args, **kwargs):
    #      context['adminform'].form.fields['course'].queryset = Course.objects.filter(name__iexact='company')
    #      return super(RegistrationAdmin, self).render_change_form(request, context, args, kwargs)


admin.site.register(Registration,RegistrationAdmin)
#
admin.site.register(Banco)
