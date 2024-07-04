from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "Número de CPF inválido."})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"O nome deve possuir apenas letras."})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': "O RG deve ter 9 caracteres"})
        # if not celular_valido(data['celular']):
        #     raise serializers.ValidationError({'celular': "O celular deve ter de 11 a 14 caracteres"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O número de celular deve atender o seguinte padrão: (xx) xxxxx-xxxx"})
        return data
    