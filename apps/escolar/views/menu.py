from django.shortcuts import render
#from usuarios.models import Usuario


def menu(request):

    usuario_logado = 21#request.user

    # Verifica se o User é staff
    # usuario_logado = Usuario.objects.get(id=usuario_logado)
    # print(f'-------------------------- {usuario_logado}')

    return render(
        request,
        'componentes/menu.html',
        # {
        #     'usuario_logado':usuario_logado,
        #     'teste_opc':'teste menu'
        # }
    )

