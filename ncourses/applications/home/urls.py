# django
from django.conf.urls import include, url

# local
from . import views


urlpatterns = [
    # urls para la aplicacion home
    url(
        r'^$',
        views.IndexView.as_view(),
        name='index'
    ),
    #url para registrar postulantes
    url(
        r'^dictar-cursos-en-ademmy/nuevo-postulante/$',
        views.PostulantCreateView.as_view(),
        name='home-nuevo_postulante'
    ),
    url(
        r'^cursos-online-de-ingenieria/bienvenido/$',
        views.TarjetaView.as_view(),
        name='home-tarjeta'
    ),
    #
    url(
        r'^templates/$',
        views.HomeView.as_view(),
        name='templates'
    ),
]
