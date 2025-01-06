from django import forms
from apps.planos.models import PrincipioDiretriz


class PrincipioDiretrizForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PrincipioDiretrizForm, self).__init__(*args, **kwargs)

    class Meta:
        model = PrincipioDiretriz
        fields = ['codigo', 'principio_diretriz', 'origem', 'criterio_priorizacao', ]
        labels = {
            'codigo': 'Código',
            'principio_diretriz': 'Princípio ou Diretriz',
            'origem': 'Origem',
            'criterio': 'Critério de Priorização?',
        }
