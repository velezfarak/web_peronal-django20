from .forms import UserCreationFormWithEmail, PerfilForm, EmailForm
from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django import forms
from .models import Perfil

# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail

    template_name = 'registration/signup.html'

    def get_success_url(self):

        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):

        form = super(SignUpView, self).get_form()
        # modifacar en tiempo real
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Nombre de Usuario' })
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2','placeholder':'Asignar correo electronico' })
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Contraseña'})
        form.fields['password2'].widget =  forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Repita la contraseña'})
        return form

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
   
    form_class = PerfilForm
    # fields = ['avatar','bio','link']
    template_name = 'registration/perfil_form.html'
    success_url = reverse_lazy('perfil')

    def get_object(self):
        # recupero el objecto
        perfil, created = Perfil.objects.get_or_create(user=self.request.user)
        return perfil

@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
   
    form_class = EmailForm
    # fields = ['avatar','bio','link']
    template_name = 'registration/email_form.html'
    success_url = reverse_lazy('perfil')

    def get_object(self):
        # recupero el objecto
        
        return self.request.user

    def get_form(self, form_class=None):

        form = super(EmailUpdate, self).get_form()
        # modifacar en tiempo real
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class':'form-control mb-2','placeholder':'Asignar Email' })
        return form




