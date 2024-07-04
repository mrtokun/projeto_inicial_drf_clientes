from rest_framework import serializers
from clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate_cpf(self, cpf):
        if len(cpf) != 11:
            raise serializers.ValidationError("O CPF deve ter 11 caracteres")
        return cpf        
    def validate_nome(self, nome):
        if not nome.isalpha():
            raise serializers.ValidationError("O nome deve possuir apenas letras.")
        return nome
    def validate_rg(selg, rg):
        if len(rg) != 9:
            raise serializers.ValidationError("O RG deve ter 9 caracteres")
        return rg
    def validate_celular(self, celular):
        if len(celular) < 11 or len(celular) > 14:
            raise serializers.ValidationError("O celular deve ter de 11 a 14 caracteres")
        return celular
    