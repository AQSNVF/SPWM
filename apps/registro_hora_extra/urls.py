from django.urls import path
from .views import (
    HoraExtraList,
    HoraExtraEdit,
    HoraExtraDelete,
    HoraExtraNovo,

    # AJAX
    HoraExtraUtilizada
)

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('edit_cad_func/<int:pk>/', HoraExtraEdit.as_view(), name='update_hora_extra'),
    path('delete/<int:pk>/', HoraExtraDelete.as_view(), name='delete_hora_extra'),
    path('Create/', HoraExtraNovo.as_view(), name='create_hora_extra'),

    # urls - AJAX
    path('utilizada-hora-extra/<int:id>/', HoraExtraUtilizada.as_view(), name='utilizada_hora_extra')

]

