from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        """
        path: template file path
        params: dictionary with parameters for rendering with a template
        filename: outuput pdf filename
        """
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(
            BytesIO(html.encode("ISO-8859-1", errors='ignore')), response
        )
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf'
            )
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)
