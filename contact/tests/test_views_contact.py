from contact.forms import ContactForm
from django.test import TestCase
from django.core import mail

class ContactGet(TestCase):
    def setUp(self):
        self.response = self.client.get('/contact/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)
    
    def test_template(self):
        self.assertTemplateUsed(self.response, 'contact/contact_form.html')
    
    def test_html(self):
        tags = (("<form", 1), ("<input", 5),('type="text"',2), ('type="email"', 1),('type="submit"', 1))
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)
    
    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_form(self):
        form = self.response.context["form"]
        self.assertIsInstance(form, ContactForm)

class ContactPostValid(TestCase):
    def setUp(self):
        data = dict(nome='Whesley Souza', email='whesley.souza@aluno.riogrande.ifrs.edu.br',mensagem='TESTANDO'  )
        self.response = self.client.post('/contact/', data);

    def test_post_valido(self): 
        self.assertEqual(302, self.response.status_code)
    
    def test_send_contact_email(self):
        self.assertEqual(1,len(mail.outbox))
    
class ContactPostInvalid(TestCase):
    def setUp(self):
        self.response = self.client.post('/contact/', {})

    def test_post_invalido(self):
        self.assertEqual(200, self.response.status_code, )

    def test_template(self):
        self.assertTemplateUsed(self.response, 'contact/contact_form.html')
    def test_form(self):
        form = self.response.context['form']
        self.assertIsInstance(form, ContactForm)

    def test_erro_form(self):
        form = self.response.context['form']
        self.assertTrue(form.errors)

class ContactSucessMessage(TestCase):
    def test_message(self):
        data = dict(nome='Whesley Souza', email='whesley.souza@aluno.riogrande.ifrs.edu.br', mensagem='TESTANDO')


        resposta = self.client.post("/contact/", data, follow=True)
        self.assertContains(resposta, 'Mensagem enviada')
