from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('abaut/', views.abaut, name='abaut'),
   
    path('store/', views.store, name='store'),
    path('sample/', views.sample, name='sample'),
    
]
