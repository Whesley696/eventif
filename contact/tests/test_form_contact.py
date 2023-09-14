from django.test import TestCase #test do django
from contact.forms import ContactForm #class

class ContactFormTest(TestCase):
    def setUp(self):
        self.form = ContactForm()

    def test_form_campo(self): #testa se a sequencia está na conformidade
        self.assertSequenceEqual(['nome',  'email', 'telefone', 'mensagem'], list(self.form.fields))

    def test_formulario_valido(self): #testa se o form é valido
        dados = dict(nome='Whesley Souza', email='whesley.souza@aluno.riogrande.ifrs.edu.br', telefone='53991401187', mensagem='HAHAHAHAHAHA')
        form = ContactForm(data=dados)
        self.assertEqual(form.is_valid(), True)

