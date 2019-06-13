from django.views.generic import CreateView
from .models import DocumentoFunc


class DocumentoFuncCreate(CreateView):
    model = DocumentoFunc
    fields = ['descricao', 'arquivo']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.proprietariofunc_id = self.kwargs['funcionario_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
