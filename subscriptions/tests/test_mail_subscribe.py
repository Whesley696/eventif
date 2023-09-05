from django.test import TestCase
from subscriptions.forms import SubscriptionForm
from django.core import mail

class MailTest(TestCase):
    def setUp(self):
        data = dict(name='Whesley Souza', cpf='05474158245', email='whesleysouza21@gmail.com', phone='53991140152')
        self.response = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]
        
    def test_subscription_email_subject(self):
        expect = "Confirmação de inscrição"
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_sender(self):
        expect = 'whesleysouza21@gmail.com'
        self.assertEqual(expect, self.email.from_email)
    
    def test_subscription_email_to(self):
        expect = ['whesleysouza21@gmail.com', 'whesleysouza21@gmail.com']  # Atualize os endereços de e-mail aqui
        self.assertEqual(expect, self.email.to)
    
    def test_subscription_email_body(self):
        contents = ['Whesley Souza','05474158245', 'whesleysouza21@gmail.com', '53991140152']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)