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
    url_video = models.URLField(blank=True)

    objects = TopicosManager()

    class Meta:
        verbose_name = 'Clase'
        verbose_name_plural = 'Clases'

    def __str__(self):
        return self.name


    #funcion que se ejecuta al guardar
    def save(self, *args, **kwargs):
        #cambiammos el formato de video
        video = self.url_video.split('/')
        self.url_video = "https://www.youtube.com/embed/"+video[3]
        #
        super(Topico, self).save(*args, **kwargs)
