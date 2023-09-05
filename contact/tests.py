from django.test import TestCase
from django.urls import reverse
from django.core import mail
from .forms import ContactForm

class ContactTests(TestCase):
    def setUp(self):
        self.valid_data = {
            'nome': 'Whesley Souza',
            'email': 'whesleysouza21@gmail.com',
            'mensagem': 'TESTANDO',
        }

    def test_get(self):
        response = self.client.get(reverse('contact_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact_form.html')

    def test_post_valido(self):
        response = self.client.post(reverse('contact_view'), data=self.valid_data)
        self.assertEqual(response.status_code, 302)

    def test_post_invalido(self):
        invalid_data = {
            'nome': '',  
            'email': 'invalid-email',  
            'mensagem': '',  
        }
        response = self.client.post(reverse('contact_view'), data=invalid_data)
        self.assertEqual(response.status_code, 200)

    def test_enviar_email(self):
        response = self.client.post(reverse('contact_view'), data=self.valid_data)
        
        self.assertEqual(response.status_code, 302)

        # Verificar se o email foi enviado e seu assunto
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'contato@eventif.com.br')