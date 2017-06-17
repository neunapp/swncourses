# -*- coding: utf-8 -*-

from django.db.models.manager import Manager


class TopicosManager(Manager):
    '''
    manager para topicos de curso
    '''

    def list_by_course(self, slug):
        '''
        recuperar los cursos mas visitados
        '''
        return self.filter(
            course__slug=slug,
        ).order_by('name')
