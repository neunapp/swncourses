# -*- coding: utf-8 -*-

from django.db.models.manager import Manager
from django.contrib.postgres.search import TrigramSimilarity

#
class RegistrationManager(Manager):
    '''
    manager para el modelo Registration o matricula
    '''

    def courses_by_user(self, usuario):
        '''
            recuperar los cursos activos de un usuario
        '''
        return self.filter(
            activate=True,
            anulate=False,
            user=usuario,
        ).order_by('-created')


    def pendiente_courses_by_user(self, usuario):
        """ devuelve curso de usuario en pre-matricula """

        return self.filter(
            activate=False,
            anulate=False,
            user=usuario,
        ).order_by('-created')
