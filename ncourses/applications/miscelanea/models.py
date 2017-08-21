# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# third-party
from model_utils.models import TimeStampedModel


from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify


@python_2_unicode_compatible
class Category(TimeStampedModel):
    """ modelo categoria de un curso """

    name = models.CharField(
        blank=True,
        max_length=200
    )
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Recomendation(TimeStampedModel):
    """ Recomendacion de los cursos """

    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Recomendacion'
        verbose_name_plural = 'Recomendaciones'

    def __str__(self):
        return self.description


@python_2_unicode_compatible
class Tag(TimeStampedModel):
    """ Tags para posicionamiento """

    name = models.CharField(blank=True, max_length=100)

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'

    def __str__(self):
        return self.name
