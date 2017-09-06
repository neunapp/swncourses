# -*- encoding: utf-8 -*-
from django import forms

#app user
from .models import Postulant


class PostulantAddForm(forms.ModelForm):
    """ formulario para registrar postulantes """

    class Meta:
        model = Postulant
        fields = (
            'full_name',
            'email',
            'phone',
            'contry',
            'city',
            'speciality',
            'url_facebook',
        )
        #
        widgets = {
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email...',
                }
            ),
            'full_name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombres...',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'numeros...',
                }
            ),
            'contry': forms.TextInput(
                attrs={
                    'placeholder': 'Pais...',
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'placeholder': 'Ciudad...',
                }
            ),
            'speciality': forms.Textarea(
                attrs={
                    'placeholder': 'Soy Experto en...',
                    'rows':'3',
                }
            ),
        }
