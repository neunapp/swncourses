# django
from django.conf.urls import include, url

# local
from . import views


urlpatterns = [
    # urls para la aplicacion home
    url(
        r'^temas-de-curso/(?P<category>[-\w]+)/(?P<slug>[-\w]+)/$',
        views.TopicoByCourseView.as_view(),
        name='topicos-by_course'
    ),
    # urls para ver una clase
    url(
        r'^cursos-clase/(?P<pk>\d+)/(?P<curso>\d+)/$',
        views.TopicoDetailView.as_view(),
        name='topicos-clase_view'
    ),
]
