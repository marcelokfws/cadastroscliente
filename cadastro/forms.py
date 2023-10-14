from django import forms

from cadastro.models import Cracha


class CrachaForm(forms.ModelForm):
    class Meta:
        model = Cracha
        fields = ['nome', 'foto', 'reds', 'endereco']


widget = {
    'foto': forms.ImageField(),
    'nome': forms.TextInput(attrs={'class': 'form-control'}),
    'reds': forms.TextInput(attrs={'class': 'form-control'}),
    'endereco': forms.TextInput(attrs={'class': 'form-control'}),

}
