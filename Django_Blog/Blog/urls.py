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
    path('guardarPost/', guardarPost, name='guardar_post'),
    path('eliminaPost/<slug>/', eliminaPost, name='elimina_post'),
    path('editaPost/<slug>/', editaPost, name='editarPost_post'),
    path('autores/', formAutorView.index, name='autores'),
   
    path('editarAutor/<autor_id>', formAutorView.edit, name='editarAutor'),
    path('eliminarAutor/<autor_id>/', formAutorView.delete, name='eliminarAutor'),
    path('updateAutor/<autor_id>/', formAutorView.update, name='updateAutor'),
    path('posts/', formPostView.index, name='posts'),
    path('altapost/', formPostView.create, name='altapost'),
     path('guardarAutor/', formAutorView.create, name='guardarAutor'),
    path('<slug:slug>/', detallePost, name='detalle_post'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

