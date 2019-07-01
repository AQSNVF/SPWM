from django.urls import path
from .views import (
    FuncionariosList,
    FuncionarioEdit,
    FuncionarioDelete,
    FuncionarioCreate,
    Pdf,
    PdfDebug
)

from.views import rel_HE_func_reportlab

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('edit/<int:pk>/', FuncionarioEdit.as_view(), name='update_funcionario'),
    path('delete/<int:pk>/', FuncionarioDelete.as_view(), name='delete_funcionario'),
    path('Create/', FuncionarioCreate.as_view(), name='create_funcionario'),
    path('rel-HE-func-reportlab', rel_HE_func_reportlab, name='rel_he_func_reportlab'),
    path('rel-HE-func-emp-xlwt', Pdf.as_view(), name='rel_he_func_emp_xlwt'),
    path('rel-HE-func-emp-xlwt_debug', PdfDebug.as_view(), name='rel_he_func_emp_xlwt_debug'),
]

