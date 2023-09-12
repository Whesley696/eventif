from django import forms

class ContactForm(forms.Form):
    nome = forms.CharField(label='nome')
    email = forms.EmailField(label='email')
    telefone = forms.CharField(label='telefone', required=False) #n é requerido
    mensagem = forms.CharField(widget=forms.Textarea)