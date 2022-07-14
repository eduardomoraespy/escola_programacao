from rest_framework import serializers

from escolar.models import VwMenuUsuario, Menu

# Serializers define the API representation.
class VwMenuUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = VwMenuUsuario
        fields = ['nome_menu','caminho']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['nome_menu','caminho']