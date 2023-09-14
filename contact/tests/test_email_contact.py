from django.test import TestCase #Test do django
from contact.forms import ContactForm # class
from django.core import mail # Mail do django

class TesteEmailContato(TestCase): # Teste para fazer o contato com o EMAIL
    def setUp(self): #Não repetição
        dados = dict(nome='Whesley Souza', email='whesley.souza@aluno.riogrande.ifrs.edu.br',  telefone='53991401187', mensagem='HAHAHAHAHAHA' ) #info
        self.response = self.client.post('/contact/', dados)  #resposta do test em post para contact com as informações
        self.email = mail.outbox[0] #primeiro email da lista outbox
        
    def test_assunto_email(self): #Teste assunto introdutorio email
        conteudo = 'Contato Feito!' 
        self.assertEqual(conteudo, self.email.subject) #compara os dois valores para ver se são iguais - 

    def test_email_enviado(self): #Teste para ver o email foi enviado
        emailEnvio = 'contato@eventif.com.br';
        self.assertEqual(emailEnvio, self.email.from_email) #compara os dois valores para ver se são iguais

    def test_email_alvo(self): #Teste para enviar o email para o email alvo
        emailAlvo = ['contato@eventif.com.br','whesley.souza@aluno.riogrande.ifrs.edu.br']  #data
        self.assertEqual(emailAlvo, self.email.to) #compara os dois valores para ver se são iguais
    
    def test_email_corpo(self): #Teste para ver se o conteudoDados está no corpo do email
        conteudoDados = ['Whesley Souza', 'whesley.souza@aluno.riogrande.ifrs.edu.br', '53991401187', 'HAHAHAHAHAHA'] 
        for content in conteudoDados:
            with self.subTest():#se CADA elemento está no CORPO DO EMAIL
                self.assertIn(content, self.email.body) #se o content for igual a x elemento
#tests adicionais
    def test_email_mensagem(self): #Teste de mensagem
        mensagem = 'HAHAHAHAHAHA'
        self.assertIn(mensagem, self.email.body) #Se a mensagem está contida no corpo do email

    def test_email_remetente(self):
        remetente = 'Whesley Souza'
        self.assertIn(remetente, self.email.body) #Se o remetente está contida no corpo do email

    def test_telefone(self):
        telefone = '53991401187'
        self.assertIn(telefone, self.email.body) #Se o telefone está contida no corpo do email
  
                