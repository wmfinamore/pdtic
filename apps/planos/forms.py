from django import forms
from apps.planos.models import PrincipioDiretriz, FonteDiretriz


class FonteDiretrizForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FonteDiretrizForm, self).__init__(*args, **kwargs)

    class Meta:
        model = FonteDiretriz
        fields = ['nome', ]
        labels = {
            'nome': 'Nome da fonte de diretrizes',
        }


class PrincipioDiretrizForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PrincipioDiretrizForm, self).__init__(*args, **kwargs)

    class Meta:
        model = PrincipioDiretriz
        fields = ['principio_diretriz', 'origem', 'criterio_priorizacao', ]
        labels = {
            'codigo': 'Código',
            'principio_diretriz': 'Princípio ou Diretriz',
            'origem': 'Origem',
            'criterio': 'Critério de Priorização?',
        }
