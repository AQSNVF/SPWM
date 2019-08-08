from django.contrib import admin
from .models import Funcionario
from .actions import ferias_marcadas, ferias_desmarcadas

class FuncionarioAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados Pessoais', {
            'classes': ('collapse',),
            'fields': (('nome', 'user'), ('cpf', 'imagem'))}),
        ('Dados Complementares', {
            'classes':('collapse',),
            'fields': ('departamentos', ('empresa', 'de_ferias'))}),
    )
    #fields = (('nome', 'user', 'cpf', 'de_ferias'), ('departamentos', 'empresa'), 'imagem')
    list_display = ('nome', 'id', 'user', 'cpf', 'foto', 'de_ferias')
    list_filter = ('departamentos', 'de_ferias')
    #search_fields = ('id', 'nome')
    #autocomplete_fields = ("funcionario.empresa",)
    actions = [ferias_marcadas, ferias_desmarcadas]
    filter_horizontal = ['departamentos',]

    def foto(self,obj):
        if obj.imagem:
            return 'Sim'
        else:
            return 'Não'
    foto.short_description = 'Foto'
#
# class DocumentosAdmin(admin.ModelAdmin):
#     list_filter = ('departamento', 'de_ferias')

admin.site.register(Funcionario, FuncionarioAdmin)
