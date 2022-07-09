from django.shortcuts import render
from usuarios.models import Usuario


def home(request):

    usuario_logado = 21#request.user
    usuario_logado = Usuario.objects.get(id=usuario_logado)

    return render(
        request,
        'home.html',
        # {
        #     'usuario_logado':usuario_logado
        # }
    )

