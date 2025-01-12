from django import forms
from .models import TipoOrigem, NecessidadeInformacao


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
