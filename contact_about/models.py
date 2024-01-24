from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone

class AboutPage(models.Model):
    image = models.ImageField(verbose_name='Image', upload_to='page_pics/')
    title = models.CharField(max_length=255, verbose_name='Title')
    text = RichTextField(verbose_name='Text')
    changed_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'About Page'
        verbose_name_plural = 'About Pages'


class AboutPageCarts(models.Model):
    icon = models.ImageField(upload_to='page_pics/', verbose_name='Image', null=True)
    page = models.ForeignKey(AboutPage, verbose_name='Page', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name='Title')
    text = models.TextField(verbose_name='Content')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Page Cart'
        verbose_name_plural = 'Page Carts'


class AboutPageStaff(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True})
    page = models.ForeignKey(AboutPage, verbose_name='Page', on_delete=models.CASCADE)
    job = models.CharField(max_length=70, verbose_name='Job')
    description = models.TextField(max_length=500)

    def __str__(self):
        return f'Staff - {self.page}'

    class Meta:
        verbose_name = 'Page staff'
        verbose_name_plural = 'Page staff'


class Contact(models.Model):
    username = models.CharField(verbose_name='Name', max_length=255)
    email = models.EmailField(verbose_name='Email')
    subject = models.CharField(max_length=120, verbose_name='Subject')
    message = models.TextField(verbose_name='Message')

    def __str__(self):
        return f'Message from {self.username}'

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'