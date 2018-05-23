from django.urls import path
from .views import SignUpView, ProfileUpdate, EmailUpdate

urlpatterns = [
    path('signup', SignUpView.as_view(), name="signup"),
    path('perfil', ProfileUpdate.as_view(), name='perfil' ),
    path('perfil/email/', EmailUpdate.as_view(), name='emailupdate' )
    
]