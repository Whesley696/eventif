from django.test import TestCase
from subscriptions.models import Subscription
from datetime import datetime

class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(name = 'Cleber Fonsceca', cpf = '1223456789', email = 'whesley.souza@aluno.riogrande.ifrs.edu.br', phone='53991140185')
        self.obj.save()
    def test_create(self):
        self.assertTrue(Subscription.objects.exists())
    
    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)
    
    def test_str(self):
        self.assertEqual('Cleber Fonsceca', str(self.obj))

    def tset_paid_default_false(self):
        self.assertEqual(False, self.obj.paid)
