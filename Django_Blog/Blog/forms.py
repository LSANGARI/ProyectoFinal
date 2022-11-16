from django import forms
from .models import Post, Autor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class formAutor(forms.ModelForm):

    class Meta:
        model=Autor
        fields = '__all__'


class formPost(forms.ModelForm):
    
    class Meta:
        model=Post
        fields = '__all__'
        exclude = ["liked"]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields = ['username','first_name', 'last_name', 'email','password1','password2']
        help_texts = {k:'' for k in fields}


class formPerfil(forms.ModelForm):

    class Meta:
        model=Autor
        fields = '__all__'
        exclude = ["username"]

