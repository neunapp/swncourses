# -*- coding: utf-8 -*-

# django
from django.views.generic import (
    DetailView,
    TemplateView,
    DeleteView,
    UpdateView,
    ListView,
    View,
)
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect

#app course
from applications.cursos.models import Course

#forms
from .forms import PreRegistrationForm
#modelos
from .models import Registration


class DashboarUserView(TemplateView):
    template_name = 'matriculas/index.html'


class PreRegistrationView(FormView):
    """ vista que registra el codigo de deposito de una matricula """

    template_name = 'matriculas/pre-registro.html'
    form_class = PreRegistrationForm
    success_url = reverse_lazy('matriculas_app:matricula-dashboard')

    def get_context_data(self, **kwargs):
        context = super(PreRegistrationView, self).get_context_data(**kwargs)
        pk_curso = self.kwargs.get('pk', 0)
        context['curso'] = Course.objects.get(pk=pk_curso)
        return context

    def form_valid(self, form):
        #recuperamos la matricula
        pk_curso = self.kwargs.get('pk', 0)
        usuario = self.request.user
        #
        matricula = Registration.objects.get(
            course__pk=pk_curso,
            user=usuario,
        )
        #actualizamos los datos
        matricula.banco = form.cleaned_data['banco']
        matricula.cod_transaction = form.cleaned_data['cod_transaction']
        matricula.save()
        print '====codigo de banco guardado correctamente===='
        return super(PreRegistrationView, self).form_valid(form)
