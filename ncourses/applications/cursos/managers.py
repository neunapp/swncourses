# -*- coding: utf-8 -*-

from django.db.models.manager import Manager


class CourseManager(Manager):
    '''
    manager para el modelo curso
    '''

    def more_visit_courses(self):
        '''
        recuperar los cursos mas visitados
        '''
        return self.filter(
            state=True,
        ).order_by('-point').order_by('-visit')
