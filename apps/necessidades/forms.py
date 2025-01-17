from django import forms
from .models import TipoOrigem, NecessidadeInformacao, TipoNecessidade, NecessidadeTI


class TipoOrigemForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TipoOrigemForm, self).__init__(*args, **kwargs)

    class Meta:
        model = TipoOrigem
        fields = ['nome', ]
        labels = {
            'nome': 'Nome',
        }


class NecessidadeInformacaoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NecessidadeInformacaoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = NecessidadeInformacao
        fields = ['codigo', 'descricao', 'estrategia_relacionada', 'origem', 'areas_relacionadas',]
        labels = {
            'codigo': 'Código',
            'descricao': 'Descrição',
            'estrategia_relacionada': 'Estratégia Relacionada',
            'origem': 'Origem',
            'areas_relacionadas': 'Áreas Relacionadas',
        }


class TipoNecessidadeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TipoNecessidadeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = TipoNecessidade
        fields = ['nome', ]
        labels = {
            'nome': 'Nome',
        }


class NecessidadeTIForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NecessidadeTIForm, self).__init__(*args, **kwargs)

    class Meta:
        model = NecessidadeTI
        fields = ['codigo', 'tipo_necessidade', 'descricao', 'estrategia_relacionada', 'origem', 'areas_relacionadas',]
        labels = {
            'codigo': 'Codigo',
            'tipo_necessidade': 'Tipo de Necessidade',
            'descricao': 'Descrição',
            'estrategia_relacionada': 'Estratégia Relacionada',
            'origem': 'Origem',
            'areas_relacionadas': 'Áreas Relacionadas',
        }
