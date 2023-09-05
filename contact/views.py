from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            telefone = form.cleaned_data['telefone']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']

            subject = 'contato@eventif.com.br'
            message = f'Nome: {nome}\nTelefone: {telefone}\nEmail: {email}\nMensagem: {mensagem}'
            from_email = email
            recipient_list = ['contato@eventif.com.br', email]

            send_mail(subject, message, from_email, recipient_list)

            return redirect('contact/')  

    else:
        form = ContactForm()

    return render(request, 'contact/contact_form.html', {'form': form})