from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('api-auth/', include('rest_framework.urls')),
    path('importer-commands', views.importer_commands, name='importer-commands'),
]
