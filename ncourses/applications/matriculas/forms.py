# -*- encoding: utf-8 -*-
from django import forms

#
from .models import Registration


#
class PreRegistrationForm(forms.ModelForm):
    """ formulario para registro de numero de deposito """

    class Meta:
        model = Registration
        fields = (
            'banco',
            'cod_transaction',
        )
        widgets = {
            'cod_transaction': forms.TextInput(
                attrs={
                    'placeholder': 'Numero de Transaccion',
                    'class':'payment-content__form__input',
                }
            ),
            'banco': forms.Select(
                attrs={
                    'class':'payment-content__form__select',
                }
            ),
        }
