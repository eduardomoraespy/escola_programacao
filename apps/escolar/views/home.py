from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from escolar.models import Menu, TipoUsuario, AssociarMenuUsuario,VwMenuUsuario

from rest_framework import viewsets, status, permissions
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import JsonResponse
from rest_framework.response import Response
from escolar.serializer import VwMenuUsuarioSerializer, MenuSerializer

from django.contrib.auth.models import User

@login_required
def home(request):

    usuario_logado = request.user.id

    return render(
        request,
        'base.html',
        {
            'usuario_logado':usuario_logado,
        }
    )


class MenuUsuarioViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    pagination_class = None

    def get_menu_usuario(self, request):

        usuario_logado = request.user
        if usuario_logado.is_superuser:
            try:
                resposta = Menu.objects.all().order_by('nome_menu')

            except ObjectDoesNotExist as error:
                return JsonResponse(error, status=status.HTTP_410_GONE)

            serializer = MenuSerializer(resposta, many=True,context={'request': request})
        
        else:
            try:
                resposta = VwMenuUsuario.objects.filter(usuario_id=usuario_logado.id)
            except ObjectDoesNotExist as error:
                return JsonResponse(error, status=status.HTTP_410_GONE)

            serializer = VwMenuUsuarioSerializer(resposta, many=True,context={'request': request})

        #print(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)
