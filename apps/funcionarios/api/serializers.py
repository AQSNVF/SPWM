from rest_framework import serializers
from apps.funcionarios.models import Funcionario
from apps.registro_hora_extra.api.serializers import RegistroHoraExtraSerializer


class FuncionarioSerializer(serializers.ModelSerializer):
    registrohoraextra_set = RegistroHoraExtraSerializer(many=True)


    class Meta:
        model = Funcionario
        fields = (
            'user_id', 'user', 'nome', 'cpf', 'imagem', 'empresa',
            'departamentos', 'registrohoraextra_set', 'total_horas_extra')
