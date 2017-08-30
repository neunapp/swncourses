# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# standard library
from datetime import timedelta, datetime


# third-party
from model_utils.models import TimeStampedModel
#
from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save

#app Cursos
from applications.cursos.models import Course

#local
from .managers import RegistrationManager


@python_2_unicode_compatible
class Banco(TimeStampedModel):
    """ Bancos registrados"""

    name = models.CharField(
        'Nombre del banco',
        blank=True,
        max_length=100
    )

    class Meta:
        verbose_name = 'Banco'
        verbose_name_plural = 'Bancos'

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Registration(TimeStampedModel):
    """ modelo para Registrar matriculas """

    course = models.ForeignKey(
        Course,
        related_name='matricula_curso',
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='alumno_curso',
        editable=False,
    )
    amount = models.DecimalField(
        'monto',
        max_digits=10,
        decimal_places=3,
        default=0,
        editable=False
    )
    banco = models.ForeignKey(
        Banco,
        related_name='banco',
        null=True,
    )
    cod_transaction = models.CharField(
        'Codigo de transaccion',
        blank=True,
        max_length=50
    )
    date_payment = models.DateTimeField(
        'Fecha Pago',
        blank=True,
        null=True
    )
    discount = models.BooleanField('con descuento',default=False)
    amount_discount = models.DecimalField(
        'Porcentaje Descuento',
        max_digits=4,
        decimal_places=1,
        default=0,
    )
    activate = models.BooleanField('Activado',default=False)
    anulate = models.BooleanField('Anulado',default=False)
    user_activate = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        editable=False,
    )

    objects = RegistrationManager()

    class Meta:
        unique_together = ("course", "user")
        verbose_name = 'Maticula'
        verbose_name_plural = 'matriculas'

    def __str__(self):
        return str(self.user.first_name)


    #funcion que se ejecuta al guardar
    def save(self, *args, **kwargs):
        #guardamos monto del curso
        curso = self.course
        self.amount = curso.price
        #verificamos si se activo
        # if self.activate:
        #     self.user_activate = self.request.user

        super(Registration, self).save(*args, **kwargs)
