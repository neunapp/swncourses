# django
from django.conf.urls import include, url

# local
from . import views


urlpatterns = [
    # urls para registrar usuarios
    url(
        r'^registro/$',
        views.UserCreateView.as_view(),
        name='user-add'
    ),
    #url para login de usuarios
    url(
        r'^login/$',
        views.LogIn.as_view(),
        name='user-login'
    ),
    #url para cerrar sesion
    url(
        r'^salir/$',
        views.LogoutView.as_view(),
        name='logout'
    ),
    #url para redireccion
    url(
        r'^redirect/(?P<pk>\d+)/$',
        views.RedirectView.as_view(),
        name='redirect'
    ),
]
