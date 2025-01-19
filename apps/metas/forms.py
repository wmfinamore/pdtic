from django import forms
from .models import Meta


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
