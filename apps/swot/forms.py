from django import forms
from apps.swot.models import TipoAmbiente


class TipoAmbienteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TipoAmbienteForm, self).__init__(*args, **kwargs)

    class Meta:
        model = TipoAmbiente
        fields = ['nome',]
        labels = {
            'nome': 'Nome',
        }
