from django import forms
from .models import UnidadeMedida, Periodicidade, Indicador

class UnidadeMedidaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UnidadeMedidaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = UnidadeMedida
        fields = ['nome', 'valor_fracionado']
        labels= {
            'nome': 'Nome',
            'valor_fracionado': 'Permite valor fracionado?',
        }


class PeriodicidadeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PeriodicidadeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Periodicidade
        fields = ['nome',]
        labels = {
            'nome': 'Nome',
        }

class IndicadorForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(IndicadorForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Indicador
        fields = ['secretaria', 'nome', 'formula', 'unidade_medida', 'responsavel', 'fonte_dados', 'resultado_atual',
                  'valor_meta', 'periodicidade', 'sentido']
        labels = {
            'secretaria': 'Secretaria',
            'nome': 'Nome',
            'formula': 'Fórmula',
            'unidade_medida': 'Unidade de Medida',
            'responsavel': 'Responsável',
            'fonte_dados': 'Fonte de Dados',
            'resultado_atual': 'Resultado atual',
            'valor_meta': 'Valor da meta',
            'periodicidade': 'Periodicidade',
            'sentido': 'Sentido',
        }
