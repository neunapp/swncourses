# django
from django.conf.urls import include, url

# local
from . import views


urlpatterns = [
    # urls para la aplicacion home
    url(
        r'^detalle-del-curso/(?P<category>[-\w]+)/(?P<slug>[-\w]+)/$',
        views.CourseDetailView.as_view(),
        name='course-detail'
    ),
]
