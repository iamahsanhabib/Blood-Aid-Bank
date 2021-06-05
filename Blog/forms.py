from django.forms import ModelForm, TextInput,Select, FileInput, DateInput,NumberInput
from Blog.models import Post
from django import forms

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','image','body1','body2',]