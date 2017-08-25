# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# third-party
from model_utils.models import TimeStampedModel

from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

#managers
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )
    TYPE_CHOICES = (
            ('0', 'Admin'),
            ('1', 'Docente'),
            ('2', 'Alumno'),
    )

    username = models.CharField('usuario', max_length=8, blank=True)
    type_user = models.CharField(
        'tipo de usuario',
        max_length=2,
        choices=TYPE_CHOICES,
        null=True,
        blank=True
    )
    email = models.EmailField('correo electronico', unique=True)
    first_name = models.CharField('nombres', max_length=50)
    last_name = models.CharField('apellidos', max_length=50)
    avatar = models.URLField(
        'foto',
        blank=True,
    )
    phone = models.CharField('telefono', max_length=50, blank=True, null=True)
    gender = models.CharField('sexo', max_length=1, choices=GENDER_CHOICES, blank=True)
    date_birth = models.DateField(blank=True, null=True)
    addresse = models.CharField('direccion',blank=True, max_length=100)

    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', ]

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return "%s %s" % (self.last_name, self.first_name)


@python_2_unicode_compatible
class Teacher(TimeStampedModel):
    """ modelo para profesor """

    user = models.ForeignKey(User)
    facebook = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    porcentaje = models.CharField(
        blank=True,
        max_length=100
    )
    state = models.BooleanField(default=False)
    about = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'

    def __str__(self):
        return str(self.user.first_name)
