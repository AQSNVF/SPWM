from django.urls import path
from .views import DocumentoFuncCreate


urlpatterns = [
     path('create_doc_func/<int:funcionario_id>/', DocumentoFuncCreate.as_view(),
          name='create_documento_func'),
    ]
