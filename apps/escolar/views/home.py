from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from usuarios.models import Usuario

@login_required
def home(request):

    usuario_logado = request.user.id
    # usuario_logado = Usuario.objects.get(id=usuario_logado)
    print(f'------------------------------- {usuario_logado}')

    return render(
        request,
        'home.html',
        {
            'usuario_logado':usuario_logado
        }
    )

