from rest_framework import viewsets, status, permissions
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import JsonResponse
from rest_framework.response import Response
from usuarios.models import Usuario
from usuarios.serializer import UsuarioSerializer




class UsuarioLogadoViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    pagination_class = None

    def get_usuario_logado(self, request):
        try:
            usuario_logado = 21#request.user

            resposta = Usuario.objects.filter(id=usuario_logado)

        except ObjectDoesNotExist as error:
            return JsonResponse(error, status=status.HTTP_410_GONE)

        serializer = UsuarioSerializer(resposta, many=True,context={'request': request})

        #print(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)