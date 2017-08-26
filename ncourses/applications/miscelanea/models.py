# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# third-party
from model_utils.models import TimeStampedModel

# standard library
from datetime import timedelta, datetime


from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify


@python_2_unicode_compatible
class Category(TimeStampedModel):
    """ modelo categoria de un curso """

    name = models.CharField(
        'Nombre Largo',
        blank=True,
        max_length=200
    )
    name_short = models.CharField(
        'Nombre Corto',
        blank=True,
        max_length=200
    )
    description = models.TextField('Descripcion',blank=True)
    slug = models.SlugField(editable=False, max_length=400)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


    #funcion que se ejecuta al guardar
    def save(self, *args, **kwargs):
        if not self.id:
            # calculamos el total de segundos de la hora actual
            now = datetime.now()
            total_time = timedelta(
                hours=now.hour,
                minutes=now.minute,
                seconds=now.second
            )
            seconds = int(total_time.total_seconds())
            slug_unique = '%s %s' % (self.name, str(seconds))
        else:
            seconds = self.slug.split('-')[-1]  # recuperamos los segundos
            slug_unique = '%s %s' % (self.name, str(seconds))

        self.slug = slugify(slug_unique)
        #
        super(Category, self).save(*args, **kwargs)


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
