from django.test import TestCase
from contact.forms import ContactForm
from django.core import mail



class TesteEmailContato(TestCase):
    def setUp(self):
        dados = dict(name='Whesley Souza', cpf='05474158245', email='whesley.souza@aluno.riogrande.ifrs.edu.br', phone='53991140152')
        self.response = self.client.post('/contato/', dados)
        self.email = mail.outbox[0]
        
    def test_assunto_email(self):
        conteudo = "Teste Contato" 
        self.assertEqual(conteudo, self.email.subject)

    def test_email_enviado(self):
        emailEnvio = 'contato@eventif.com.br' 
        self.assertEqual(emailEnvio, self.email.from_email)
    def test_email_alvo(self):
        emailAlvo = ['contato@eventif.com.br','whesley.souza@aluno.riogrande.ifrs.edu.br']  
        self.assertEqual(emailAlvo, self.email.to)
    
    def test_email_corpo(self):
        dados = ['Whesley Souza', '53991140152',  'whesley.souza@aluno.riogrande.ifrs.edu.br', 'TESTANDO'] 
        for content in dados:
            with self.subTest():
                self.assertIn(content, self.email.body)