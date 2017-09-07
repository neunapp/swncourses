# django
from django.conf.urls import include, url

# local
from . import views


urlpatterns = [
    # urls para la aplicacion curso

    #url para ver informacion de curso
    url(
        r'^articulos-y-tutoriales-en-ingenieria/(?P<category>[-\w]+)/$',
        views.BlogListView.as_view(),
        name='blog-list'
    ),
    #url para ver blog-articulo
    url(
        r'^ver-blogs-de-ingenieria/(?P<slug>[-\w]+)/$',
        views.BlogDetailView.as_view(),
        name='blog-detail'
    )
]
