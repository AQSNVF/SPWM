from django.urls import path
from .views import (
    DepartamentosList,
    DepartamentosCreate,
    DepartamentosUpdate,
    DepartamentosDelete
)

urlpatterns = [
    path('list', DepartamentosList.as_view(), name='list_departamentos'),
    path('create', DepartamentosCreate.as_view(), name='create_departamento'),
    path('update/<int:pk>', DepartamentosUpdate.as_view(), name='update_departamento'),
    path('delete/<int:pk>', DepartamentosDelete.as_view(), name='delete_departamento')
    ]


