# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# third-party
from model_utils.models import TimeStampedModel

# standard library
from datetime import timedelta, datetime
#
from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
#

@python_2_unicode_compatible
class Suscription(TimeStampedModel):
    """ Suscripcion de usuarios """

    email = models.EmailField()

    class Meta:
        verbose_name = 'Suscripcion'
        verbose_name_plural = 'Suscritos'

    def __str__(self):
        return self.email


@python_2_unicode_compatible
class Postulant(TimeStampedModel):
    """ modelo para postulntes a profesor """

    full_name = models.CharField(
        'Nombres',
        max_length=200
    )
    email = models.EmailField()
    phone = models.CharField(
        'Telefonos',
        blank=True,
        max_length=20
    )
    contry = models.CharField(
        'Paiz',
        blank=True,
        max_length=100
    )
    city = models.CharField(
        'Ciudad',
        blank=True,
        max_length=100
    )
    speciality = models.TextField('Especialidad')
    url_facebook = models.URLField(blank=True)
    url_linkedin = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Postulante a Maestro'
        verbose_name_plural = 'Postulantes a Instructor'

    def __str__(self):
        return self.full_name
