# -*- coding: utf-8 -*-
# django
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.views.generic import ListView

# django
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    DetailView,
    TemplateView,
    DeleteView,
    UpdateView,
    ListView,
    CreateView,
    View
)

#mixns
from applications.mixins import IsAutemticateMixin

#aplicacion cursos
from applications.cursos.models import Course

#models
from .models import Postulant, Suscription
#forms
from .forms import PostulantAddForm


class IndexView(IsAutemticateMixin, TemplateView):
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


class TarjetaView(TemplateView):
    '''
     vista que muestra un tajeta de bienvenida
    '''

    template_name = 'home/tarjeta.html'


class PostulantCreateView(CreateView):
    model = Postulant
    form_class = PostulantAddForm
    success_url = reverse_lazy('home_app:home-tarjeta')
    template_name = 'home/postulante.html'
