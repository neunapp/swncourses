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

#applications miscelanea
from applications.miscelanea.models import Category

#local
from .models import Course
from .forms import SearchForm


class CourseDetailView(DetailView):
    """vita para ver el detalle de un curso"""
    model = Course
    template_name = 'course/detail.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['temas'] = Topico.objects.list_by_course(
            self.get_object().slug
        )
        #
        return context


class CoursesSearchView(ListView):
    """ vista para buscar cursos """
    context_object_name = 'courses'
    model = Course
    template_name = 'course/search.html'

    def get_context_data(self, **kwargs):
        context = super(CoursesSearchView, self).get_context_data(**kwargs)
        context['form'] = SearchForm
        context['other_courses'] = Course.objects.other_courses()
        context['categorys'] = Category.objects.all()
        return context

    def get_queryset(self):
        #recuperamos el valor por GET
        print '------'
        print self.kwargs['category']
        q = self.request.GET.get("kword", '')
        queryset = Course.objects.search_courses(q,'todo',0)
        return queryset
