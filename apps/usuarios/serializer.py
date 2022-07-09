from rest_framework import serializers

from usuarios.models import Usuario

# Serializers define the API representation.
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','email']