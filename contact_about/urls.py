from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_about, name='main_about'),
    path('contact/', views.index_contact, name='contact')
]