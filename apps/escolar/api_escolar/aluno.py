from rest_framework import viewsets, status, permissions
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import JsonResponse
from rest_framework.response import Response
from escolar.serializer import AlunosSerializer
from escolar.models import Aluno


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunosSerializer
    pagination_class = None

    def get_consulta_aluno(self, request):
        try:

            resposta = Aluno.objects.all().order_by('nome')

        except ObjectDoesNotExist as error:
            return JsonResponse(error, status=status.HTTP_410_GONE)

        serializer = AlunosSerializer(resposta, many=True,context={'request': request})

        #print(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)