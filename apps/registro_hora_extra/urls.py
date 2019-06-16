from django.urls import path
from .views import (
    HoraExtraList,
    HoraExtraEdit,
    HoraExtraDelete,
    HoraExtraNovo,

    # AJAX
    HoraExtraUtilizada,

    # urls - CSV
    Exportar_Para_CSV,
    Exportar_Para_XLS
)

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('edit_cad_func/<int:pk>/', HoraExtraEdit.as_view(), name='update_hora_extra'),
    path('delete/<int:pk>/', HoraExtraDelete.as_view(), name='delete_hora_extra'),
    path('Create/', HoraExtraNovo.as_view(), name='create_hora_extra'),

    # urls - AJAX
    path('utilizada-hora-extra/<int:id>/', HoraExtraUtilizada.as_view(), name='utilizada_hora_extra'),

    # urls - CSV e XLS
    path('exportar-csv/', Exportar_Para_CSV.as_view(), name='exportar_csv'),
    path('exportar-xls/', Exportar_Para_XLS.as_view(), name='exportar_xls'),
]

