from django.test import TestCase
from contact.forms import ContactForm

class ContactFormTest(TestCase):
    def setUp(self):
        self.form = ContactForm()

    def test_form_campo(self):
        self.assertSequenceEqual(['nome',  'email', 'telefone', 'mensagem'], list(self.form.fields))