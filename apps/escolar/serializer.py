from rest_framework import serializers

from escolar.models import VwMenuUsuario, Menu, Aluno

# Serializers define the API representation.
class VwMenuUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = VwMenuUsuario
        fields = ['nome_menu','caminho']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['nome_menu','caminho']


class AlunosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ('__all__')