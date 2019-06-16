from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Funcionario
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)

import io
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas

from django.views.generic.base import View, TemplateView
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa

class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'cpf', 'departamentos']


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'cpf', 'departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioCreate, self).form_valid(form)


def rel_HE_func_reportlab(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachement; filename="RelFunc001.pdf"'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)




    funcionarios = Funcionario.objects.filter(empresa=request.user.funcionario.empresa)

    p.drawString(10, 810, "Relação de H.E. dos Funcionarios.")
    p.drawString(10, 790, '' * 87)

    str_ = 'Empresa: %s '
    p.drawString(10, 780, str_ % (request.user.funcionario.empresa))


    str_ = 'Nome: %s | Horas no Banco de Extra: %.2f'

    p.drawString(10, 770, '. ' * 87)
    p.drawString(10, 760, '' * 87)

    y = 750
    for funcionario in funcionarios:
        p.drawString(10, y, str_ % (funcionario.nome,
                    funcionario.total_horas_extra))
        y -= 20

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response

#
# def rel_HE_func_emp_reportlab(request):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachement; filename="RelFuncemp001.pdf"'
#
#     buffer = io.BytesIO()
#     p = canvas.Canvas(buffer)
#
#     p.drawString(10, 810, "Relação de H.E. dos Funcionarios.")
#
#     funcionarios = Funcionario.objects.all()
#
#
#     str_ = 'Empresa: %s >|Nome: %s | Hora Extra: %.2f'
#
#
#
#     p.drawString(10, 790, '. ' * 87)
#
#     y = 780
#     for funcionario in funcionarios:
#         p.drawString(10, y, str_ % (funcionario.empresa,
#             funcionario.nome, funcionario.total_horas_extras))
#         y -= 20
#
#     p.showPage()
#     p.save()
#
#     pdf = buffer.getvalue()
#     buffer.close()
#     response.write(pdf)
#
#     return response

class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)

class Pdf(View):

    def get(self, request):
        params = {
            'today': 'variavel today',
            'sales': 'variavel sales',
            'request': request,
        }
        return Render.render('funcionarios/relatorio.html', params, 'myfile')


class PdfDebug(TemplateView):
    template_name = 'funcionarios/lista_funcionarios.html'