from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core import mail
from django.template.loader import render_to_string
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def create(request):
    form = ContactForm(request.POST)

    if not form.is_valid():
        return render(request, 'contact/contact_form.html', {'form': form})
    assunto = 'Contato Feito!'
    remetente = settings.DEFAULT_FROM_EMAIL
    destinatario = form.cleaned_data['email']
    template = 'contact/contact_email.txt'
    dados_form = form.cleaned_data
    _send_mail(assunto, remetente, destinatario, template, dados_form)

    messages.success(request, 'Mensagem enviada')
    

    return HttpResponseRedirect('/contact/')

def new(request):
    return render(request, 'contact/contact_form.html', {'form': ContactForm()})

def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_, to])
