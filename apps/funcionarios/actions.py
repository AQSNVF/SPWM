def ferias_marcadas(modeladmin, request, queryset):
    queryset.update(de_ferias=True)

ferias_marcadas.short_description = "Férias marcadas"


def ferias_desmarcadas(modeladmin, request, queryset):
    queryset.update(de_ferias=False)

ferias_desmarcadas.short_description = "Férias desmarcadas"