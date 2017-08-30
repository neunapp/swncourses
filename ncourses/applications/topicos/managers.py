# -*- coding: utf-8 -*-

from django.db.models.manager import Manager


class TopicosManager(Manager):
    '''
    manager para topicos de curso
    '''

    def list_by_course(self, slug):
        '''
        recuperar los temas de un curso
        '''
        return self.filter(
            course__slug=slug,
        ).order_by('name')
