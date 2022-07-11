from rest_framework import serializers

from django.contrib.auth.models import User

# Serializers define the API representation.
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']