"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#from django.urls import include, path
from django.urls import path

from apuntapp.views import AutorListView, ModuloListView, PublicacionListView, CicloListView, PublicacionDetailView

urlpatterns = [
    #path('apuntapp/', include('apuntapp.urls')),
    path('admin/', admin.site.urls),
    #path('')
    path('autor/',AutorListView.as_view()),
    path('modulo/',ModuloListView.as_view()),
    path('publicacion/',PublicacionListView.as_view()),
    path('ciclo/',CicloListView.as_view()),

    path('publicacion/<int:pk>/',PublicacionDetailView.as_view(), name='publicacion-detail'),
]