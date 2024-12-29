from django import forms
from .models import TipoCompetencia, Competencia, Desenvolvedor, NivelCompetencia,InventarioCompetencia


class TipoCompetenciaoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TipoCompetenciaoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = TipoCompetencia
        fields = '__all__'
        labels = {
            'tipo_competencia': 'Tipo de Competência',
            'descricao': 'Descrição',
        }


class CompetenciaoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CompetenciaoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Competencia
        fields = '__all__'
        labels = {
            'tipo_competencia': 'Tipo de Competência',
            'competencia': 'Nome da Competência',
            'descricao': 'Descrição da Competência',
        }


class DesenvolvedorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DesenvolvedorForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Desenvolvedor
        fields = '__all__'
        labels = {
            'nome': 'Nome Completo',
            'email': 'E-mail',
            'matricula': 'Matrícula',
            'ativo': 'Ativo?',
        }


class NivelCompetenciaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NivelCompetenciaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = NivelCompetencia
        fields = '__all__'
        labels = {
            'nivel': 'Nível da Competência',
            'descricao': 'Descrição do Nível',
        }


class InventarioCompetenciaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(InventarioCompetenciaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = InventarioCompetencia
        fields = '__all__'
        labels = {
            'desenvolvedor': 'Desenvolvedor',
            'competencia': 'Competência',
            'aquisicao_competencia': 'Relato da aquisição da competência',
            'nivel': 'Nivel da Competência',
        }
