from django.test import TestCase
from django.urls import reverse
from django.core import mail
from .forms import ContactForm

class TestesContato(TestCase):
    def setUp(self):
        self.dados_validos = {
            'nome': 'Whesley Souza', 'email': 'whesley.souza@aluno.riogrande.ifrs.edu.br',  'mensagem': 'TESTANDO'
        }

    def test_get(self):
        response = self.client.get(reverse('contact_view'))
        self.assertEqual(response.status_code, 200);
        self.assertTemplateUsed(response, 'contact/contact_form.html')

    def test_post_valido(self):
        response = self.client.post(reverse('contact_view'), data=self.dados_validos)
        self.assertEqual(response.status_code, 302)

    def test_post_invalido(self):
        dados_invalidos = {
            'nome': '', 'email': 'invalid-email', 'mensagem': 'invalido';
        }
        response = self.client.post(reverse('contact_view'), data=dados_invalidos)
        self.assertEqual(response.status_code, 200)

    def test_enviar_email(self):
        response = self.client.post(reverse('contact_view'), data=self.dados_validos)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 1);
        self.assertEqual(mail.outbox[0].subject, 'contato@eventif.com.br')
