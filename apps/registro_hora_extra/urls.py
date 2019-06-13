from django.urls import path
from .views import (
    HoraExtraList,
    HoraExtraEdit,
    HoraExtraDelete,
    HoraExtraNovo
)

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('edit/<int:pk>/', HoraExtraEdit.as_view(), name='update_hora_extra'),
    path('delete/<int:pk>/', HoraExtraDelete.as_view(), name='delete_hora_extra'),
    path('Create/', HoraExtraNovo.as_view(), name='create_hora_extra'),
]

