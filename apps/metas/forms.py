from django import forms
from .models import Meta, Acao


class MetasForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MetasForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Meta
        fields = ['nome', 'necessidades', 'indicadores', 'valor_meta', 'prazo', ]
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
        fields = ['metas', 'nome', 'areas_responsaveis', 'data_inicio_estimada',
                  'data_conclusao_estimada', 'quantidade_pessoas', 'competencias', 'valor_investimento',
                  'valor_custeio']
        labels = {
            'codigo': 'Código',
            'metas': 'Metas',
            'nome': 'Nome',
            'areas_responsaveis': 'Áreas responsáveis',
            'data_inicio_estimada': 'Data de Início Estimada',
            'data_conclusao_estimada': 'Data de Conclusão Estimada',
            'quantidade_pessoas': 'Quantidade de Pessoas',
            'competencias': 'Competências',
            'valor_investimento': 'Valor da Investimento',
            'valor_custeio': 'Valor de Custeio',
        }
