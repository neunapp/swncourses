# -*- coding: utf-8 -*-

from django.db.models.manager import Manager
from django.contrib.postgres.search import TrigramSimilarity


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


    def other_courses(self):
        '''
        recuperar lista de cursos a mostrar si no hay resultado de busqueda
        '''
        return self.filter(
            state=True,
        ).order_by('-point').order_by('-visit')


    def search_courses(self, kword, category, price):
        '''
        recuperar los cursos por palabra clave
        '''

        if category == 'todo':
            category = ''

        consulta = self.filter(
            state=True,
            category__name__icontains=category,
        )

        # nombre
        query1 = consulta.filter(
            name__trigram_similar=kword
        ).order_by('-visit')
        #descripcion corta
        query2 = consulta.filter(
            description_short__trigram_similar=kword
        ).order_by('-visit')
        # tag
        query3 = consulta.filter(
            tags__name__trigram_similar=kword
        ).order_by('-visit')

        #resultado
        return (query1 | query2 | query3).distinct()
