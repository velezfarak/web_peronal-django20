from django.test import TestCase
from .models import Perfil
from django.contrib.auth.models import User

# Create your tests here.

class TestPerfilCase(TestCase):
    def setup(self):
        User.objects.create_user('test','test@user.com','test1234')

    def test_perfil_exists():
        exists = User.objects.filter(user__username = 'test').exists()    
        self.assertEqual(exists,True)
        