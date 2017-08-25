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
]
