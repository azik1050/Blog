from django import forms
from .models import PostComment, Post, PostCategory


class PostCommentForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control mb-4',
        'rows': 6
    }))
    class Meta:
        model = PostComment
        fields = ('message',)


class PostForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(queryset=PostCategory.objects.all())
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    slug = forms.SlugField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'rows': 3
    }))
    published = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        'class': 'form-control'
    }))
    class Meta:
        model = Post
        fields = ('category', 'title', 'slug', 'description', 'content', 'image', 'published')


