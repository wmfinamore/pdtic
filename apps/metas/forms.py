from django import forms
from .models import Meta, Acao


class MetasForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MetasForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Meta
        fields = ['codigo', 'nome', 'necessidades', 'indicador', 'valor_meta', 'prazo', ]
        labels = {
            'codigo': 'Codigo',
            'nome': 'Nome',
            'necessidades': 'Necessidades',
            'indicador': 'Indicador',
            'valor_meta': 'Valor da meta',
            'prazo': 'Prazo',
        }


class AcaoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AcaoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Acao
        fields = ['codigo', 'metas', 'nome', 'areas_responsaveis', 'data_inicio_estimada',
                  'data_conclusao_estimada']
        labels = {
            'codigo': 'Código',
            'metas': 'Metas',
            'nome': 'Nome',
            'areas_responsaveis': 'Áreas responsáveis',
            'data_inicio_estimada': 'Data de Início Estimada',
            'data_conclusao_estimada': 'Data de Conclusão Estimada',
        }
