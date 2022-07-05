from django.shortcuts import render
from escolar.forms import aluno
from escolar.models import *


def lista_aluno(request):

    titulo = 'Lista de Alunos'
    query_aluno = Aluno.objects.all()

    return render(
        request,
        'aluno/lista_aluno.html',
        {
            'titulo':titulo,
            'query_aluno':query_aluno
        }
    )


def cadastro_aluno(request):

    titulo = 'Cadastro Aluno'
    usuario_logado = request.user

    form = aluno.CadastroAlunoForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()



    return render(
        request,
        'aluno/cadastro_aluno.html',
        {
            'form':form,
            'titulo':titulo
        }
    )

def atualiza_aluno(request):

    return render(
        request,
        'index.html'
    )