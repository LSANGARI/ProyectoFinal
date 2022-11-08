from django import forms
from .models import Post, Categoria, Autor

class formAutor(forms.ModelForm):

    class Meta:
        model=Autor
        fields = '__all__'

class formPost(forms.ModelForm):
    
    class Meta:
        model=Post
        fields = '__all__'


