from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Blog'

urlpatterns = [
    path('', home, name='index'),
    path('generales/', generales,  name='generales'),
    path('programacion/', programacion,  name='programacion'),
    path('videojuegos/', videojuegos,  name='videojuegos'),
    path('tecnologia/', tecnologia,  name='tecnologia'),
    path('tutoriales/', tutoriales,  name='tutoriales'),
    path('aboutus/', aboutus,  name='aboutus'),
    path('<slug:slug>/', detallePost, name='detalle_post'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)