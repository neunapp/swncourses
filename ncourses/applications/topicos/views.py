# -*- coding: utf-8 -*-

# django
from django.views.generic import (
    DetailView,
    TemplateView,
    DeleteView,
    UpdateView,
    ListView,
)
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect

#app course
from applications.cursos.models import Course

# local
from .models import Topico


class TopicoByCourseView(ListView):
    """ lista de temas por curso """
    context_object_name = 'temas'
    template_name = 'topicos/list.html'

    def get_context_data(self, **kwargs):
        context = super(TopicoByCourseView, self).get_context_data(**kwargs)
        context['curso'] = Course.objects.get(slug=self.kwargs['slug'])
        return context

    def get_queryset(self):
        slug = self.kwargs['slug']
        queryset = Topico.objects.list_by_course(slug)
        return queryset


class TopicoDetailView(DetailView):
    """ vista que muestra el tema en reproducion de video """
    model = Topico
    template_name = 'topicos/clase.html'

    def get_context_data(self, **kwargs):
        context = super(TopicoDetailView, self).get_context_data(**kwargs)
        pk_curso = self.kwargs.get('curso', 0)
        curso = Course.objects.get(pk=pk_curso)
        context['curso'] = curso
        context['temas'] = Topico.objects.list_by_course(curso.slug)
        return context
