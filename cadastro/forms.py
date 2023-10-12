from django import forms

from cadastro.models import Cracha


class CrachaForm(forms.ModelForm):
    class Meta:
        model = Cracha
        fields = ['nome', 'foto']
