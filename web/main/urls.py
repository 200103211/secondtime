from django.urls import path, include
from django.urls import *
from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    # path('about', views.about, name='about'),
    # path('projects', views.projects, name='projects'),
    # path('contact', views.contact, name='contact'),
    path('register/', views.register),
    path('', views.reg),
    path('user/', views.user),
    path('contact/', views.contact_view),
    path('success/', views.success_view, name='success'),
]

