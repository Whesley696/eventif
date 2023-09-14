from contact.forms import ContactForm #class
from django.test import TestCase #test do django
from django.core import mail #mail do django

class ContactGet(TestCase): #testa o GET do APP contact
    def setUp(self):
        self.response = self.client.get('/contact/') #testa o GET do clientcom o contact

    def test_get(self):
        self.assertEqual(200, self.response.status_code) #verifica se o o STATUSCODE do response é igual a 200 (get)
    
    def test_template(self): #Teste do TEMPLATE
        self.assertTemplateUsed(self.response, 'contact/contact_form.html') #testa se o TEMPLATE usado é o mesmo que o ESPERADO
    
    def test_html(self): #Testa oHTML Utilizado
        tags = (("<form", 1), ("<input", 5),('type="text"',2), ('type="email"', 1),('type="submit"', 1))
        for text, count in tags: #TESTA se cada TAG Está de acordo no html esperado
            with self.subTest():
                self.assertContains(self.response, text, count)
    
    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken') #verifica se a string está contida no resposta

    def test_form(self): #test get do formulario
        form = self.response.context["form"]
        self.assertIsInstance(form, ContactForm) #verifica se o FORM é uma instancia da class importada

class ContactPostValid(TestCase): #TESTS DE POST VALIDOS
    def setUp(self):
        data = dict(nome='Whesley Souza', email='whesley.souza@aluno.riogrande.ifrs.edu.br',mensagem='TESTANDO'  )
        self.response = self.client.post('/contact/', data)

    def test_post_valido(self): #test de POST VALIDO-
        self.assertEqual(302, self.response.status_code) #compara OS STATUS CODE (DOIS VALORES)
    
    def test_num_contato(self): #TESTA AS CONTAGENS de emails enviados para certo contato
        self.assertEqual(1,len(mail.outbox))

    def test_mensagem_email(self): #test de mensagem
        email = mail.outbox[0]
        self.assertIn('TESTANDO', email.body)
    
class ContactPostInvalid(TestCase): #teste post invalido
    def setUp(self):
        self.response = self.client.post('/contact/', {}) #um post vazio

    def test_post_invalido(self):
        self.assertEqual(200, self.response.status_code, ) #compara OS STATUS CODE (DOIS VALORES)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'contact/contact_form.html') #testa se o TEMPLATE usado é o mesmo que o da resposta
    def test_form(self): #
        form = self.response.context['form']
        self.assertIsInstance(form, ContactForm)

    def test_erro_form(self):
        form = self.response.context['form']
        self.assertTrue(form.errors) #verifica se há erros

class ContactSucessMessage(TestCase):
    def test_message(self):
        data = dict(nome='Whesley Souza', email='whesley.souza@aluno.riogrande.ifrs.edu.br', mensagem='TESTANDO')
        resposta = self.client.post("/contact/", data, follow=True)
        self.assertContains(resposta, 'Mensagem enviada') #verifica se a string tem na resposta esperada (response)
