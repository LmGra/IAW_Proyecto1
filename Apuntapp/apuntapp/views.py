
from django.views.generic import ListView, DetailView
from apuntapp.models import Autor, Modulo, Publicacion, Ciclo


class AutorListView(ListView):
    model = Autor
class ModuloListView(ListView):
    model = Modulo
class PublicacionListView(ListView):
    model = Publicacion
class CicloListView(ListView):
    model = Ciclo

class PublicacionDetailView(DetailView):
    model = Publicacion



#from django.shortcuts import render

#from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
