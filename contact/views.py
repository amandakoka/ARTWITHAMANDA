from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import ContactMessage


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
 
            send_mail(
                f'Contact Form Submission from {contact_message.name}',
                contact_message.message,
                contact_message.email,
                [settings.EMAIL_HOST_USER],
            )
            return redirect('contact:success')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})


def success_view(request):
    return render(request, 'contact/success.html')
