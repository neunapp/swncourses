# django
from django.conf.urls import include, url

# local
from . import views


urlpatterns = [
    # urls para la aplicacion curso

    #url para ver informacion de curso
    url(
        r'^detalle-del-curso/(?P<category>[-\w]+)/(?P<slug>[-\w]+)/$',
        views.CourseDetailView.as_view(),
        name='course-detail'
    ),

    # urls para vista buscar curso
    url(
        r'^buscar-curso/(?P<category>[-\w]+)/$',
        views.CoursesSearchView.as_view(),
        name='course-search'
    ),
]
