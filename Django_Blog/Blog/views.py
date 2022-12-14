import os
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import formAutor, formPost, UserRegisterForm, formPerfil
from django.conf import settings
#from django.urls import reverse_lazy
from .models import Post, Categoria, Autor, User

from django.contrib import messages

#from django.views.generic.edit import formAutor


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


def detallePost(request,id):
    post = get_object_or_404(Post,id = id)
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



class formAutorView(HttpRequest):

    def index(request):
        # autor = formAutor()
        # autores = Autor.objects.all()
        autor = UserRegisterForm()
        autores = Autor.objects.all()
        return render(request, 'autores.html', {'form':autor, 'autores':autores})

    def create(request):
        # autor = formAutor(request.POST)
        # if autor.is_valid():
        #     autor.save()
        #     autores = Autor.objects.all()
        #     autor=formAutor()
        autor = UserRegisterForm(request.POST)
        if autor.is_valid():
            autor.save()
            autores = Autor.objects.all()
            autor=UserRegisterForm()

        return render(request, 'autores.html', {'form':autor, 'autores':autores, 'mensaje':'OK' })
        #return redirect(request.META['HTTP_REFERER'])



    def delete(request, autor_id):
        autor = User.objects.get(pk=autor_id)
        autor.delete()
        autores = Autor.objects.all()
        autor = UserRegisterForm()
        return render(request, 'autores.html', {'form':autor, 'autores':autores})

    def edit(request, autor_id):
        autor = Autor.objects.filter(id=autor_id).first()
        form = formPerfil(instance=autor)   
        return render(request, 'editarAutor.html', {'form':form, 'autor':autor, })

    def perfil(request, user_id):
        autor = Autor.objects.filter(username_id=user_id).first()
        form = formPerfil(instance=autor)   
        return render(request, 'perfil.html', {'form':form, 'autor':autor, })

    def guardarperfil(request, user_id):
        autor= Autor.objects.get(username_id=user_id)
        form = formPerfil(request.POST, instance=autor)
        if form.is_valid():
             form.save()
             autor = formPerfil() 
        return render(request, 'perfil.html', {'form':form, 'autor':autor, })

    def update(request, autor_id):
        autor= Autor.objects.get(pk=autor_id)
        form = formAutor(request.POST, instance=autor)
        if form.is_valid():
            form.save()
        autores = Autor.objects.all()  
        autor = formAutor() 
        return render(request, 'autores.html', {'form':autor, 'autores':autores}) 

class formPostView(HttpRequest):

    def index(request):
        user = request.user
        initial_data={
            'autor':user, 
        }
        post = formPost(initial=initial_data)
        return render(request, 'posts.html', {'form':post})

    def create(request):
        post = formPost(request.POST, request.FILES)
        slug=request.POST['slug'].replace(" ", "_")
        if post.is_valid():
            post.save(commit=False)   
            post.instance.slug= slug
            post.save()
            post=formPost()
        return render(request, 'posts.html', {'mensaje':'OK', 'form':post})

    def edit(request, slug):


        post = Post.objects.filter(slug=slug).first()
        form = formPost(instance=post)   
        return render(request, 'editarpost.html', {'form':form, 'post':post, })

    def delete(request, post_id):
        posts = Post.objects.get(id=post_id)
        path = str(posts.imagen)
        document_root= str(settings.MEDIA_ROOT)
        fullpath = (document_root + "/" + path).replace('/', '\\')
        os.remove(fullpath)
        posts.delete()
        return redirect ('/')

    def update(request, post_id):
        post= Post.objects.get(pk=post_id)
        path = str(post.imagen)
        document_root= str(settings.MEDIA_ROOT)
        fullpath = (document_root + "/" + path).replace('/', '\\')

        form = formPost(request.POST, request.FILES, instance=post)
        slug=request.POST['slug'].replace(" ", "_")

        if form.is_valid():
            
            if request.POST.get('imagen')=='':
                form.save(commit=False)  
                form.instance.slug= slug
                post.save()
                form = formPost() 
                return redirect ('/')
            else:
                 os.remove(fullpath)
                
                 imagen = request.FILES['imagen']

                 form.save(commit=False)  
                 form.instance.slug= slug
                 form.instance.imagen = imagen
                 post.save()
                 form = formPost() 
                 return redirect ('/')

def register(request):
        if request.method ==  'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.instance.is_staff=True 
                form.save()
                username = form.cleaned_data['username']
                messages.success(request, f'Usuario {username} creado Correctamente')
                return redirect('/login/')
                #return redirect(request.META.get('HTTP_REFERER'))
        else:
            form= UserRegisterForm()
        context = {'form': form}
        return render(request, 'register.html/', context)


def like_post(request):
    user = request.user
  
    if request.method =='POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        # like, created = Like.objects.get_or_create(autor_id=user.id, postid=post_id)

        # if not created:
        #     if like.value == 'Like':
        #         like.value= 'Unlike'
        #     else:
        #         like.value= 'Like'

        #like.save()

    #return redirect ('/')
    return redirect(request.META.get('HTTP_REFERER'))
