from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        return create(request);
    else:
        return new(request);

def create(request):
    form = ContactForm(request.POST)

    if not form.is_valid():
        return render(request, 'contact/contact_form.html', {'form': form})

    nome = form.cleaned_data['nome'];
    telefone = form.cleaned_data['telefone']
    email = form.cleaned_data['email'];
    mensagem = form.cleaned_data['mensagem']

    assunto = 'contato@eventif.com.br'  ;
    remetente = email  ;
    lista_destinatarios = ['contato@eventif.com.br', email]  

    conteudo_email = render_to_string('contact/contact_email.txt', {  'nome': nome,'telefone': telefone,'email': email, 'mensagem': mensagem
    })

    send_mail(assunto, conteudo_email, remetente, lista_destinatarios)

    messages.success(request, 'Mensagem enviada com sucesso');
    return HttpResponseRedirect('/contact/')

def new(request):
    return render(request, 'contact/contact_form.html', {'form': ContactForm()});
