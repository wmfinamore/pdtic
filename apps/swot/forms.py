from django import forms
from apps.swot.models import TipoAmbiente, TipoAvaliacao, Swot


class TipoAmbienteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TipoAmbienteForm, self).__init__(*args, **kwargs)

    class Meta:
        model = TipoAmbiente
        fields = ['nome',]
        labels = {
            'nome': 'Nome',
        }


class TipoAvaliacaoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TipoAvaliacaoForm, self).__init__(*args, **kwargs)

    class Meta:
        model = TipoAvaliacao
        fields = ['tipo_ambiente', 'nome',]
        labels = {
            'tipo_ambiente': 'Tipo de Ambiente',
            'nome': 'Nome',
        }


class SwotForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SwotForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Swot
        fields = ['tipo_ambiente', 'tipo_avaliacao', 'descricao',]
        labels = {
            'tipo_ambiente': 'Tipo de Ambiente',
            'tipo_avaliacao': 'Tipo de Avaliacao',
            'descricao': 'Descrição',
        }
