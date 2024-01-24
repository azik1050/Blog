from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class PostCategory(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Name')
    slug = models.SlugField(verbose_name='Identificator', max_length=70, unique=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Post Category'
        verbose_name_plural = 'Post Categories'


class Post(models.Model):
    category = models.ManyToManyField(PostCategory)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')
    title = models.CharField(max_length=50, verbose_name='Title')
    slug = models.SlugField(max_length=60, verbose_name='Identificator', unique=True)
    description = models.CharField(max_length=255, verbose_name='Short description')
    content = RichTextField(verbose_name='Content')
    posted_at = models.DateTimeField(verbose_name='First Published At', default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='Updated at', auto_now=True)
    published = models.BooleanField(default=True, verbose_name='Status')
    image = models.ImageField(verbose_name='Image', upload_to='blog_pics/')

    def get_absolute_url(self):
        return reverse('main_post', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'


class PostComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='pcom')
    message = models.TextField()
    sent_at = models.DateTimeField(default=timezone.now)



