from django.test import TestCase
from subscriptions.forms import SubscriptionForm
from django.core import mail

class SubscribeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')

    def test_get(self):
        """GET /inscricao/ must return status_code 200"""
        self.assertEqual(200, self.response.status_code)
    
    def test_template(self):
        """Must use subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')
    
    def test_html(self):
        """HTML must contain input tags"""
        self.assertContains(self.response, "<form")
        self.assertContains(self.response, "<input", 6)
        self.assertContains(self.response, 'type="text"',3)
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')
    
    def test_csrf(self):
        """HTML must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.response.context["form"]
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        form = self.response.context['form']
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))

class SubscribeTestPost(TestCase):
    def setUp(self):
        data = dict(name='Whesley Souza', cpf='05474158245', email='whesleysouza21@gmail.com', phone='53991140152')
        self.response = self.client.post('/inscricao/', data)

    def test_post(self): 
        self.assertEqual(302, self.response.status_code)
    
    def test_send_subscribe_email(self):
        self.assertEqual(1, len(mail.outbox))
    
    def test_subscription_email_subject(self):
        email = mail.outbox[0]
        expect = "Confirmação de inscrição"
        self.assertEqual(expect, email.subject)

    def test_subscription_email_sender(self):
        email = mail.outbox[0]
        expect = 'whesleysouza21@gmail.com'
        self.assertEqual(expect, email.from_email)
    
    def test_subscription_email_to(self):
        email = mail.outbox[0]
        expect = ['patricksouza@gmail.com', 'whesleysouza21@gmail.com']  # Atualize os endereços de e-mail aqui
        self.assertEqual(expect, email.to)
    
    def test_subscription_email_body(self):
        email = mail.outbox[0]
        self.assertIn('Whesley Souza', email.body)
        self.assertIn('05474158245', email.body)
        self.assertIn('whesleysouza21@gmail.com', email.body)
        self.assertIn('53991140152', email.body)

class SubscribeInvalidPost(TestCase):
    def setUp(self):
        self.response = self.client.post('/inscricao/', {})

    def test_post(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_error(self):
        form = self.response.context['form']
        self.assertTrue(form.errors)

class SubscribeSucessMessage(TestCase):
    def test_message(self):
        data = dict(name='Whesley Souza', cpf='05474158245', email='whesleysouza21@gmail.com', phone='53991140152')

        response = self.client.post("/inscricao/", data, follow=True)
        self.assertContains(response, 'Inscrição realizada com sucesso')
