from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Categoria, Autor
#from django.conf import settings
from django.db.models import Q
from django.core.paginator import Paginator
#from django.utils.datastructures import MultiValueDictKeyError



# Create your views here.

def home(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True)
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()

    paginator = Paginator(posts,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'index.html',{'posts':posts})


def detallePost(request,slug):
    post = get_object_or_404(Post,slug = slug)
    return render(request,'post.html',{'detalle_post':post})

def generales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'General')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'General'),
        ).distinct()

    paginator = Paginator(posts,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'generales.html',{'posts':posts})

def programacion(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Programacion')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Programacion'),
        ).distinct()

    paginator = Paginator(posts,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'programacion.html',{'posts':posts})

def tutoriales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Tutoriales')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Tutoriales'),
        ).distinct()

    paginator = Paginator(posts,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'tutoriales.html',{'posts':posts})

def tecnologia(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Tecnologia')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Tecnologia'),
        ).distinct()

    paginator = Paginator(posts,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'tecnologia.html',{'posts':posts})

def videojuegos(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Videojuegos')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Videojuegos'),
        ).distinct()

    paginator = Paginator(posts,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'videojuegos.html',{'posts':posts})

def aboutus(request):
    return render (request, 'aboutus.html')


def editaPost(request, slug):
    posts = Post.objects.get(slug=slug)
    autores = Autor.objects.all()
    categorias= Categoria.objects.all
    return render (request, 'editarpost.html/', {'detalle_post':posts , 'lista_autores':autores, 'categorias':categorias, })

def guardarPost(request):

    id =request.POST['id']
    titulo =request.POST['titulo']
    slug = request.POST['slug']
    descripcion = request.POST['descripcion']
    contenido = request.POST['contenido']
    #ver el tema de no modifica el img
    imagen = request.FILES['imagen']
    autor = request.POST['autor']
    categoria = request.POST['categoria']


    if 'estado' in request.POST: 
        estado = True 
    else: estado = False


    post = Post.objects.get(id=id)

    post.titulo = titulo
    post.slug = slug
    post.descripcion = descripcion
    post.contenido = contenido
    post.imagen = imagen
    post.autor = Autor(id=autor)
    post.categoria = Categoria(id=categoria)
    post.estado = estado

    post.save()
    return redirect ('/')

 
def eliminaPost(request, slug):
    posts = Post.objects.get(slug=slug)
    posts.delete()
    return redirect ('/')

def cruds(request):
    autores = Autor.objects.all()

    if request.method =='POST':
         nombre =request.POST['nombre']
         apellido = request.POST['apellido']
         linkedin = request.POST['linkedin']
         git = request.POST['git']
         email = request.POST['email']
         #activo = request.POST['activo']
         if 'activo' in request.POST: 
            activo = True 
         else: 
            activo = False

         autor = Autor.objects.create(nombre=nombre, apellido=apellido, linkedin=linkedin, git=git, correo=email, estado=activo)
         
    return render (request, 'cruds.html/', {'autores':autores} )