from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('std/', views.std),
    #path('view/', views.view, name='view'),
    #path('delete/<int:id>', views.delete),
    #path('edit/<int:id>', views.edit),
    path('', include('main.urls')),
]
