
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from apuntapp.models import Autor, Modulo, Publicacion, Ciclo
from django.urls import reverse_lazy


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



class PublicacionCreateView(CreateView):
    model = Publicacion
    fields = ['titulo', 'comentario', 'archivo', 'modulo', 'autor']

class PublicacionUpdateView(UpdateView):
    model = Publicacion
    fields = ['titulo', 'comentario']
    template_name_sufix = '_update_form'

class PublicacionDeleteView(DeleteView):
    model = Publicacion
    success_url = reverse_lazy('publicacion-list')



#from django.shortcuts import render

#from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
