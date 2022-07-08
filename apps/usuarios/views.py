from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password
from usuarios.models import *
from usuarios.form import CadastroUsuarioForm, DetailUsuarioForm, EditaUsuarioForm

from django.contrib import messages

def lista_usuario(request):

    titulo = 'Lista de Usuários'
    query_usuario = Usuario.objects.all()

    return render(
        request,
        'usuario/lista_usuario.html',
        {
            'titulo':titulo,
            'query_usuario':query_usuario
        }
    )

def cadastro_usuario(request):

    titulo = 'Cadastro de Usuário'
    form = CadastroUsuarioForm()

    if request.method == "POST":
        form = CadastroUsuarioForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            #instance.password = make_password(instance.password)
            print(f'senha usuario --------------- {instance.password}')
            instance.save()

            ## solução para impressão de mensagem de sucesso no front-end

            messages.success(
                request, 
                f'Usuário {instance.email} Registrado com Sucesso'
            )

            return redirect('cadastro_usuario')

    return render(
        request,
        'usuario/cadastro_usuario.html',
        {
            'titulo':titulo,
            'form':form,
        }
    )


def detail_usuario(request, id):

    titulo = 'Detalhes do Usuário'

    usuario_obj = get_object_or_404(Usuario, id=id)

    form = DetailUsuarioForm(instance=usuario_obj)

    return render(
        request,
        'usuario/detail_usuario.html',
        {
            'titulo':titulo,
            'form':form
        }
    )

def edita_usuario(request, id):

    titulo = 'Editar Usuário'
    usuario_obj = get_object_or_404(Usuario, id=id)
    print(f'----------------------------- usuario_obj {usuario_obj.password}')
    form = EditaUsuarioForm(request.POST or None, instance=usuario_obj)


    if form.is_valid():
        instance = form.save(commit=False)
        #instance.password = make_password(instance.password)
        instance.save()

        messages.success(
            request, f'Usuário {instance.email} atualizado com Sucesso'
        )

        return redirect('lista_usuario')
    

    return render(
        request,
        'usuario/edita_usuario.html',
        {
            'titulo':titulo,
            'form':form,
        }
    )

def remove_usuario(request, id):
    usuario_obj = get_object_or_404(Usuario, id=id)

    try:
        usuario_obj.delete()

        messages.success(
            request, f'Usuário "{usuario_obj.email}" removido com sucesso'
        )
    except Exception as error:
        messages.error(
            request, f'Usuário "{usuario_obj.nome}" não pode ser removido'
        )

    return redirect('lista_usuario')