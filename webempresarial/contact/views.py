from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.

def contact(request):
   
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            content = request.POST.get('content')
            # suponemos que todo va bien redireccionamos
            emails = EmailMessage(
                'La Cafettiera: nuevo mensaje de contacot',
                'De {}, <{}>\n\nEscribio {}'.format(name,email,content),
                'no contestar@inbox.mailtrap.io',
                ['velezfarak@gmail.com','velezfarak@yahoo.es'],
                reply_to=[email]
            )
            try:
                emails.send()
                # todo a ido bien ok
                return redirect(reverse('contact')+'?ok')
            except:
                # algo no ha ido bien FAIL
                return redirect(reverse('contact')+'?fail')    



    return render(request, 'contact/contact.html', {'form':contact_form})  
