from django.contrib import admin
from .models import Post, PostCategory

class PostCategoryAdmin(admin.ModelAdmin):
    fields = (('name', 'slug'),)
    list_display = ('name', 'slug')
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class PostAdmin(admin.ModelAdmin):
    fields = (
        ('title', 'slug'),
        ('category', 'author'),
        'description', 'content', 'posted_at', 'published', 'image'
    )
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'published')
    list_editable = ('published',)
    list_filter = ('category', 'author', 'published')
    list_display_links = ('title',)
    search_fields = ('title',)




admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Post, PostAdmin)