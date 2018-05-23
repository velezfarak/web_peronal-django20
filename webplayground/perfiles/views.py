from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import Perfil 

# Create your views here.

# Create your views here.
class PerfilListView(ListView):
    model = Perfil
    template_name = 'perfiles/perfil_list.html'
    paginate_by = 3

class PerfilDetailView(DetailView):
    model = Perfil
    template_name = 'perfiles/perfil_detail.html'

    def get_object(self):
        return get_object_or_404(Perfil, user__username=self.kwargs['username'])
      
