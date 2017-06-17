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
]
