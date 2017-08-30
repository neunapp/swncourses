# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#mixns
from applications.mixins import IsAutemticateMixin

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
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

#app curso
from applications.cursos.models import Course

#app matriculas
from applications.matriculas.models import Registration
from applications.matriculas.functions import (
    create_matricula_free,
    create_update_registration
)

from .models import User
#
from .forms import UserAddForm, LoginForm


class UserCreateView(IsAutemticateMixin, CreateView):
    """ vista para registrar usuarios """

    template_name = 'users/register.html'
    success_url = reverse_lazy('matriculas_app:matricula-dashboard')
    form_class = UserAddForm

    def form_valid(self, form):
        #recuperamos el usuario y guardamos
        usuario = form.save(commit=False)
        password = form.cleaned_data['password1']
        usuario.set_password(password)
        usuario.type_user = '2'
        usuario.save()
        user = authenticate(
            username = form.cleaned_data['email'],
            password = form.cleaned_data['password1'],
        )
        return super(UserCreateView, self).form_valid(form)


class LogIn(IsAutemticateMixin, FormView):
    """ vista para acceso de usuarios login """

    template_name = 'users/login.html'
    success_url = '.'
    form_class = LoginForm

    def form_valid(self, form):
        print '*******************'
        # Verfiamos si el usuario y contrasenha son correctos.
        user = authenticate(
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )

        if user is not None:
            if user.is_active and user.type_user == '2':
                login(self.request, user)
                return HttpResponseRedirect(
                    reverse(
                        'matriculas_app:matricula-dashboard'
                    )
                )
            else:
                return HttpResponseRedirect(
                    reverse(
                        'users_app:user-login'
                    )
                )

class LogoutView(View):
    """
    cerrar sesion
    """
    url = '/auth/login/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'users_app:user-login'
            )
        )


class RedirectView(LoginRequiredMixin, View):
    """ direccionar dependiendo de consulta """

    login_url = reverse_lazy('users_app:user-login')

    def get(self, request, *args, **kwargs):
        #recuperamos pk de curso
        pk_course = self.kwargs['pk']
        #recuperamos curso
        curso = Course.objects.get(pk=pk_course)
        #verificamos si ya esta matriculado
        if Registration.objects.filter(course=curso, activate=True).exists():
            return HttpResponseRedirect(
                reverse(
                    'matriculas_app:matricula-dashboard'
                )
            )
        elif curso.price == 0:
            create_matricula_free(curso, self.request.user)
            return HttpResponseRedirect(
                reverse(
                    'matriculas_app:matricula-dashboard'
                )
            )
        else:
            create_update_registration(curso, request.user)
            return HttpResponseRedirect(
                reverse(
                    'matriculas_app:matricula-preinscripcion',
                    kwargs={
                        'pk': curso.pk
                    },
                )
            )

        return self.render_to_response(self.get_context_data())
