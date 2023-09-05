from django import forms

class ContactForm(forms.Form):
    nome = forms.CharField(label='nome')
    telefone = forms.CharField(label='telefone', required=False) #n é requerido
    email = forms.EmailField(label='email')
    mensagem = forms.CharField(widget=forms.Textarea)