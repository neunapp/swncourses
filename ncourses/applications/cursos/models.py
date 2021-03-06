# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# standard library
from datetime import timedelta, datetime


# third-party
from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField


from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save


#applications miscelanea
from applications.miscelanea.models import (
    Category,
    Tag,
    Recomendation
)

#app user
from applications.users.models import Teacher


#local
from .signals import save_url_image
from .managers import CourseManager


@python_2_unicode_compatible
class Course(TimeStampedModel):
    """ modelo para Cursos """

    NIVEL_CHOICES = (
        ('0', 'Basico'),
        ('1', 'Intermedio'),
        ('2', 'Avanzado'),
    )
    #
    name = models.CharField(
        'Nombre Curso',
        max_length=100,
    )
    category = models.ForeignKey(
        Category,
        related_name='Categoria'
    )
    price = models.DecimalField(
        'Precio',
        max_digits=10,
        decimal_places=3,
    )
    video = models.URLField(
        'Video introductorio',
        blank=True
    )
    image = models.ImageField(
        upload_to='curso',
        verbose_name='imagen_curso',
        blank=True,
        null=True,
    )
    image_url = models.URLField(blank=True)
    description_short = models.TextField(
        'Descripcion corta',
        blank=True,
    )
    description_large = RichTextUploadingField(
        'Descripcion larga',
        null=True,
        blank=True,
    )
    resume = RichTextUploadingField(
        'Resumen',
        null=True,
        blank=True,
    )
    recomendation = models.ForeignKey(
        Recomendation,
        related_name='Recomendacion',
    )
    teacher = models.ForeignKey(
        Teacher,
        related_name='userio_profesor',
        blank=True,
        null=True,
    )
    state = models.BooleanField('Publicar',default=False)
    point = models.IntegerField('Puntaje',default=0)
    visit = models.IntegerField('Visitas',default=0)
    tags = models.ManyToManyField(Tag)
    nivel = models.CharField('Nivel', max_length=1, choices=NIVEL_CHOICES)
    slug = models.SlugField(editable=False, max_length=400)

    objects = CourseManager()

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.name

    #funcion para validar campos
    def clean(self):
        #verificams que almenos image or image_upload se ingrese
        if ((self.image_url == None) and (self.image == None)):
            raise ValidationError(
                {'image':'Ingrese url de imagen o cargue la imagen de su ordenador'}
            )
        else:
            print 'CORRECTO'

    #funcion que se ejecuta al guardar
    def save(self, *args, **kwargs):
        #cambiammos el formato de video
        video = self.video.split('/')
        self.video = "https://www.youtube.com/embed/"+video[3]
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
        super(Course, self).save(*args, **kwargs)
