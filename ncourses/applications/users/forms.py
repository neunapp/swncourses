# -*- encoding: utf-8 -*-
from django import forms

from django.contrib.auth import authenticate

#app user
from .models import User


class LoginForm(forms.Form):

    email = forms.CharField(
        label='Email',
        max_length='100',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email',
                'autofocus': 'autofocus',
            }
        ),
    )
    password = forms.CharField(
        label='contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'password',
            }
        ),
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('email o password incorrectos.')
        return self.cleaned_data


class UserAddForm(forms.ModelForm):
    """ formulario para registrar usuarios """

    password1 = forms.CharField(
        label='contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'password',
            }
        ),
    )
    password2 = forms.CharField(
        label='contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'password',
            }
        ),
    )

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
        )
        #
        widgets = {
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombres...',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Apellidos...',
                }
            ),
        }

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'las contraseñas no coinciden..!!')
        elif len(password2) < 5:
            print 'menor a 5 caracteres'
            self.add_error(
                'password2',
                'la contraseña debe tener por lo menos 5 caracteres!!'
            )
        else:
            return password2
