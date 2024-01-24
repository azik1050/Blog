from django.contrib import admin
from .models import AboutPage, AboutPageCarts, AboutPageStaff, Contact


class AboutPageCartsInline(admin.TabularInline):
    model = AboutPageCarts
    extra = 1


class AboutPageStaffInline(admin.TabularInline):
    model = AboutPageStaff
    extra = 1


class AboutPageAdmin(admin.ModelAdmin):
    fields = (('image', 'title'), 'text')
    inlines = [AboutPageCartsInline, AboutPageStaffInline]


class ContactAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'subject')
    list_display_links = ('username',)
    search_fields = ('username',)
    list_filter = ('username', 'email')


admin.site.register(AboutPage, AboutPageAdmin)
admin.site.register(Contact, ContactAdmin)