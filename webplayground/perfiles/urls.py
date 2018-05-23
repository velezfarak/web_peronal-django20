from django.urls import path
from .views import PerfilListView, PerfilDetailView

perfil_patters = ([
    path('',PerfilListView.as_view(),name='list'),
    path('<username>/', PerfilDetailView.as_view(), name='detail')


],"perfiles")