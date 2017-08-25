# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# django
from django.views.generic.edit import FormView
from django.views.generic import (
    DetailView,
    TemplateView,
    DeleteView,
    UpdateView,
    ListView,
    CreateView,
)
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from .models import User
#
from .forms import UserAddForm, LoginForm


class UserCreateView(CreateView):
    """ vista para registrar usuarios """

    template_name = 'users/register.html'
    success_url = '.'
    form_class = UserAddForm

    def form_valid(self, form):
        #recuperamos el usuario y guardamos
        usuario = form.save(commit=False)
        password = form.cleaned_data['password1']
        usuario.set_password(password)
        usuario.type_user = '2'
        usuario.save()
        return super(UserCreateView, self).form_valid(form)


class LogIn(FormView):
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
                        'users_app:user-add'
                    )
                )
            else:
                return HttpResponseRedirect(
                    reverse(
                        'users_app:login'
                    )
                )
