from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField('Nombre de la Categoria', max_length=100, null =False,blank = False)
    estado = models.BooleanField('Activada/ No Activada', default=True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE,  null=True, blank=True)
    nombre = models.CharField('Nombre Autor', max_length=255, null= False, blank=False)
    apellido = models.CharField('Apellido Autor', max_length=255, null= False, blank=False)
    linkedin = models.URLField('linkedin', null=True, blank=True)
    git = models.URLField('git', null=True, blank=True)
    correo = models.EmailField('Email', null=False, blank=False)
    estado = models.BooleanField('Activo/No Activo', default = True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now = False,auto_now_add = True)

    class Meta:
        verbose_name='Autor'
        verbose_name_plural='Autores'

    def __str__(self):
        return "{0},{1}".format(self.apellido, self.nombre)


class Post(models.Model):
    titulo = models.CharField('Titulo', max_length=90, null= False, blank=False)
    slug = models.CharField('Slug', max_length=100, null= False, blank=False)
    descripcion = models.CharField('Descripcion', max_length=110, null= False, blank=False)
    contenido = RichTextField ('Contenido')
    imagen = models.ImageField('Imagen', null= False, blank=False, upload_to='images/')
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default = True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now = False, auto_now_add = True)
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')

    class Meta:
        verbose_name='Post'
        verbose_name_plural='Posts'

    def __str__(self):
        return self.titulo

    @property
    def num_likes(self):
        return self.liked.all().count()

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model):
    autor = models.ForeignKey(Autor, on_delete = models.CASCADE)
    postid = models.ForeignKey(Post, on_delete = models.CASCADE)
    valor = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now = False, auto_now_add = True)

    class Meta:
        verbose_name='Like'
        verbose_name_plural='Likes'

    def __str__(self):
        return str(self.post)