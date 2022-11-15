from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

app_name = 'Blog'

urlpatterns = [
    path('', home, name='index'),
    path('generales/', generales,  name='generales'),
    path('programacion/', programacion,  name='programacion'),
    path('videojuegos/', videojuegos,  name='videojuegos'),
    path('tecnologia/', tecnologia,  name='tecnologia'),
    path('tutoriales/', tutoriales,  name='tutoriales'),
    path('aboutus/', aboutus,  name='aboutus'),
    path('guardarPost/<post_id>/', formPostView.update, name='guardar_post'),
    path('eliminaPost/<post_id>/', formPostView.delete, name='elimina_post'),
    path('editaPost/<slug>/', formPostView.edit, name='editarPost_post'),
    path('autores/', formAutorView.index, name='autores'),
    path('editarAutor/<autor_id>', formAutorView.edit, name='editarAutor'),
    path('perfilAutor/<user_id>', formAutorView.perfil, name='perfilAutor'),
    path('guardarPerfilAutor/<user_id>', formAutorView.guardarperfil, name='guardarPerfilAutor'),
    path('eliminarAutor/<autor_id>/', formAutorView.delete, name='eliminarAutor'),
    path('updateAutor/<autor_id>/', formAutorView.update, name='updateAutor'),
    path('posts/', formPostView.index, name='posts'),
    path('altapost/', formPostView.create, name='altapost'),
    path('guardarAutor/', formAutorView.create, name='guardarAutor'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('<id>/', detallePost, name='detalle_post'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

