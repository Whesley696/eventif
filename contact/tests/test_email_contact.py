from django.test import TestCase
from contact.forms import ContactForm
from django.core import mail

class TesteEmailContato(TestCase):
    def setUp(self):
        dados = dict(nome='Whesley Souza', email='whesley.souza@aluno.riogrande.ifrs.edu.br',  telefone='53991401187', mensagem='HAHAHAHAHAHA' )
        self.response = self.client.post('/contact/', dados)  
        self.email = mail.outbox[0]
        
    def test_assunto_email(self):
        conteudo = 'Contato Feito!'
        self.assertEqual(conteudo, self.email.subject)

    def test_email_enviado(self):
        emailEnvio = 'contato@eventif.com.br' 
        self.assertEqual(emailEnvio, self.email.from_email)

    def test_email_alvo(self):
        emailAlvo = ['contato@eventif.com.br','whesley.souza@aluno.riogrande.ifrs.edu.br']  
        self.assertEqual(emailAlvo, self.email.to)
    
    def test_email_corpo(self):
        conteudoDados = ['Whesley Souza', 'whesley.souza@aluno.riogrande.ifrs.edu.br', '53991401187', 'HAHAHAHAHAHA'] 
        for content in conteudoDados:
            with self.subTest():
                self.assertIn(content, self.email.body)
                