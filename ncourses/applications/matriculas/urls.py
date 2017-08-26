# django
from django.conf.urls import include, url

# local
from . import views


urlpatterns = [
    #url para dasboard de usuarios
    url(
        r'^dasboard/$',
        views.DashboarUserView.as_view(),
        name='matricula-dashboard'
    ),

    # urls para pantalla pre-inscripcion
    url(
        r'^pre-inscripcion/(?P<pk>\d+)/$',
        views.PreRegistrationView.as_view(),
        name='matricula-preinscripcion'
    ),
]
