# -*- coding: utf-8 -*-
# django
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView


#aplicacion cursos
from applications.cursos.models import Course


class IndexView(TemplateView):
    '''
    Pagina principal mostrar cursos mas visitdos
    '''

    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['cursos'] = Course.objects.more_visit_courses()
        #
        return context


class HomeView(TemplateView):
    '''
    Pagina para probar template
    '''

    template_name = 'home/index.html'
