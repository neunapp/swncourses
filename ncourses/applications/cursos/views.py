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

#aplicacion topicos
from applications.topicos.models import Topico

#local
from .models import Course


class CourseDetailView(DetailView):
    model = Course
    template_name = 'course/detail.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['temas'] = Topico.objects.list_by_course(
            self.get_object().slug
        )
        #
        return context
