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

# local
from .models import Topico


class TopicoByCourseView(ListView):
    """ lista de temas por curso """
    context_object_name = 'temas'
    template_name = 'topicos/list.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        queryset = Topico.objects.list_by_course(slug)
        return queryset
