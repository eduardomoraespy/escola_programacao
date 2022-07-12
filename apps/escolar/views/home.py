from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):

    usuario_logado = request.user.id

    return render(
        request,
        'home.html',
        {
            'usuario_logado':usuario_logado
        }
    )

