from django.shortcuts import render, redirect, get_object_or_404
from escolar.models import *
from usuarios.models import Usuario
from escolar.forms.aluno import CadastroAlunoForm, DetailAlunoForm, EditaAlunoForm

from django.contrib import messages

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

    titulo = 'Cadastro de Aluno'
    form = CadastroAlunoForm()
    usuario_logado = 21#request.user

    # Verifica se o User é staff
    query_user_staff = Usuario.objects.get(id=usuario_logado)

    if query_user_staff.is_staff:
        if request.method == "POST":
            form = CadastroAlunoForm(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.usuarioID = usuario_logado
                instance.save()

                messages.success(
                    request, 
                    f'Aluno {instance.nome} registrado com Sucesso'
                )

                return redirect('cadastro_aluno')
    else:
        messages.warning(
            request, 
            f'Usuário não é permitido cadastrar Aluno'
        )
        return redirect('home')

    return render(
        request,
        'aluno/cadastro_aluno.html',
        {
            'titulo':titulo,
            'form':form,
        }
    )

def detail_aluno(request, id):

    titulo = 'Detalhes do Aluno'
    aluno_obj = get_object_or_404(Aluno, id=id)
    form = DetailAlunoForm(instance=aluno_obj)

    return render(
        request,
        'aluno/detail_aluno.html',
        {
            'titulo':titulo,
            'form':form
        }
    )

def edita_aluno(request, id):

    titulo = 'Editar Aluno'
    aluno_obj = get_object_or_404(Aluno, id=id)
    form = EditaAlunoForm(request.POST or None, instance=aluno_obj)
    usuario_logado = 21#request.user

    # Verifica se o User é staff
    query_user_staff = Usuario.objects.get(id=usuario_logado)

    if query_user_staff.is_staff:
        if form.is_valid():
            instance = form.save(commit=False)
            #instance.usuarioID = usuario_logado
            instance.save()

            messages.success(
                request, f'Aluno {instance.nome} atualizado com Sucesso'
            )

            return redirect('lista_aluno')
    else:
        messages.warning(
            request, 
            f'Aluno não é permitido atualizar professor'
        )
        return redirect('home')
    

    return render(
        request,
        'aluno/edita_aluno.html',
        {
            'titulo':titulo,
            'form':form,
        }
    )

def remove_aluno(request, id):
    aluno_obj = get_object_or_404(Aluno, id=id)

    try:
        aluno_obj.delete()

        messages.success(
            request, f'Aluno "{aluno_obj.nome}" removido com sucesso'
        )
    except Exception as error:
        messages.error(
            request, f'Aluno "{aluno_obj.nome}" não pode ser removido'
        )

    return redirect('lista_aluno')