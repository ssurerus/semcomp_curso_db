from django import forms
from .models import Inscricao, Curso

class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ['nome_completo', 'matricula', 'email', 'curso']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'descricao']