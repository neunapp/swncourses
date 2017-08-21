# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# third-party
from model_utils.models import TimeStampedModel

from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify

#applications cursos
from applications.cursos.models import Course

#local
from .managers import TopicosManager


@python_2_unicode_compatible
class Topico(TimeStampedModel):
    """ modelo para un tema o topicos """

    course = models.ForeignKey(
        Course,
        related_name='Curso',
    )
    name = models.CharField(
        blank=True,
        max_length=200
    )
    description = models.TextField(blank=True)
    minutes = models.CharField(
        blank=True,
        max_length=100
    )

    objects = TopicosManager()

    class Meta:
        verbose_name = 'Tema'
        verbose_name_plural = 'Temas'

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Video(TimeStampedModel):
    """ Almacena url de video """

    url_video = models.URLField(blank=True)
    minutes = models.CharField(
        blank=True,
        max_length=10
    )

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return self.minutes
