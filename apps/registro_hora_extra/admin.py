from django.contrib import admin
from .models import RegistroHoraExtra


class RegistroHoraExtraAdmin(admin.ModelAdmin):
    fields = ('motivo', 'funcionario', 'horas', 'utilizada')
    list_display = ('motivo', 'funcionario', 'horas', 'utilizada')



admin.site.register(RegistroHoraExtra, RegistroHoraExtraAdmin)

