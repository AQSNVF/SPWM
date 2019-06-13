from django.urls import path
from .views import (
    FuncionariosList,
    FuncionarioEdit,
    FuncionarioDelete,
    FuncionarioCreate
)

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('edit/<int:pk>/', FuncionarioEdit.as_view(), name='update_funcionario'),
    path('delete/<int:pk>/', FuncionarioDelete.as_view(), name='delete_funcionario'),
    path('Create/', FuncionarioCreate.as_view(), name='create_funcionario'),
]

