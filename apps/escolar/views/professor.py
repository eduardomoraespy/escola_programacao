from django.shortcuts import render, redirect, get_object_or_404
from escolar.models import *
from usuarios.models import Usuario
from escolar.forms.professor import CadastroProfessorForm, DetailProfessorForm, EditaProfessorForm

from django.contrib import messages

def lista_professor(request):

    titulo = 'Lista de Professores'
    query_usuario = Professor.objects.all()

    return render(
        request,
        'professor/lista_professor.html',
        {
            'titulo':titulo,
            'query_usuario':query_usuario
        }
    )

def cadastro_professor(request):

    titulo = 'Cadastro de Professor'
    form = CadastroProfessorForm()
    usuario_logado = request.user

    # Verifica se o User é staff
    #query_user_staff = Usuario.objects.get(id=usuario_logado.id)

    print(f'--------------------- {usuario_logado} ------------------ {usuario_logado}')

    if request.method == "POST":
        form = CadastroProfessorForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            messages.success(
                request, 
                f'Professor {instance.nome} registrado com Sucesso'
            )

            return redirect('cadastro_professor')

    return render(
        request,
        'professor/cadastro_professor.html',
        {
            'titulo':titulo,
            'form':form,
        }
    )

def detail_professor(request, id):

    titulo = 'Detalhes do Professor'
    professor_obj = get_object_or_404(Professor, id=id)
    form = DetailProfessorForm(instance=professor_obj)

    return render(
        request,
        'professor/detail_professor.html',
        {
            'titulo':titulo,
            'form':form
        }
    )

def edita_professor(request, id):

    titulo = 'Editar Professor'
    professor_obj = get_object_or_404(Professor, id=id)
    form = EditaProfessorForm(request.POST or None, instance=professor_obj)


    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

        messages.success(
            request, f'Professor {instance.nome} atualizado com Sucesso'
        )

        return redirect('lista_professor')
    

    return render(
        request,
        'usuario/edita_usuario.html',
        {
            'titulo':titulo,
            'form':form,
        }
    )

def remove_usuario(request, id):
    professor_obj = get_object_or_404(Professor, id=id)

    try:
        professor_obj.delete()

        messages.success(
            request, f'Professor "{professor_obj.nome}" removido com sucesso'
        )
    except Exception as error:
        messages.error(
            request, f'Professor "{professor_obj.nome}" não pode ser removido'
        )

    return redirect('lista_professor')