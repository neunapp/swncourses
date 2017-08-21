"""ncourses URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # urls para la aplicacion home
    url(r'^', include('applications.home.urls', namespace="home_app")),
    url(r'^', include('applications.cursos.urls', namespace="cursos_app")),
    url(r'^', include('applications.topicos.urls', namespace="topicos_app")),

    #
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
