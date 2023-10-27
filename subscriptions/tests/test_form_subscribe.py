from django.test import TestCase
from subscriptions.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):

    def test_form_has_fields(self):
        form = SubscriptionForm()
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))

    def test_cpf_has_digits(self):
        form = self.make_validated_form(cpf='ABCD5678901')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        form = self.make_validated_form(cpf='123456') 
        self.assertFormErrorCode(form, 'cpf', 'length')


    def test_name_must_be_capitalized(self):
        form = self.make_validated_form(name= 'WHESLEY souza')
        self.assertEqual('Whesley Souza', form.cleaned_data['name'])

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        error_list = errors[field]
        exception = error_list[0]
        self.assertEqual(code, exception.code)

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        error_list = errors[field]
        self.assertListEqual([msg], error_list)

    def make_validated_form(self, **kwargs):
        valid_data = dict(name='Whesley Souza', cpf='05385269323', email='whesley.souza@aluno.riogrande.ifrs.edu.br', phone='53-91140187')
        data = dict(valid_data, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()

        return form
