from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from escolar.models import *
from django.contrib.auth.models import User
from escolar.forms.curso import CadastroCursoForm, DetailCursoForm, EditaCursoForm, MatriculaCursoForm

@login_required
def lista_curso(request):

    titulo = 'Lista de Cursos'
    query_curso = Curso.objects.all()
    paginator = Paginator(query_curso, 5)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    usuario_logado = request.user
    query_user_staff = User.objects.get(id=usuario_logado.id)

    return render(
        request,
        'curso/lista_curso.html',
        {
            'titulo':titulo,
            'query_curso':query_curso,
            'query_user_staff':query_user_staff,
            'page_obj': page_obj
        }
    )

@login_required
def cadastro_curso(request):

    titulo = 'Cadastro de Curso'
    form = CadastroCursoForm()
    usuario_logado = request.user

    # Verifica se o User é staff
    query_user_staff = User.objects.get(id=usuario_logado.id)

    if query_user_staff.is_staff:
        if request.method == "POST":
            form = CadastroCursoForm(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.usuario_id = usuario_logado
                instance.save()

                messages.success(
                    request, 
                    f'Curso "{instance.nome_curso}" registrado com Sucesso'
                )

                return redirect('cadastro_curso')
    else:
        messages.warning(
            request, 
            f'Usuário não é permitido cadastrar curso'
        )
        return redirect('home')

    return render(
        request,
        'curso/cadastro_curso.html',
        {
            'titulo':titulo,
            'form':form,
        }
    )

@login_required
def detail_curso(request, id):

    titulo = 'Detalhes do Curso'
    curso_obj = get_object_or_404(Curso, id=id)
    form = DetailCursoForm(instance=curso_obj)

    return render(
        request,
        'curso/detail_curso.html',
        {
            'titulo':titulo,
            'form':form
        }
    )

@login_required
def edita_curso(request, id):

    titulo = 'Editar Professor'
    curso_obj = get_object_or_404(Curso, id=id)
    form = EditaCursoForm(request.POST or None, instance=curso_obj)
    usuario_logado = request.user

    # Verifica se o User é staff
    query_user_staff = User.objects.get(id=usuario_logado.id)

    if query_user_staff.is_staff:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.usuario_id = usuario_logado.id
            instance.save()

            messages.success(
                request, f'Curso "{instance.nome_curso}" atualizado com Sucesso'
            )

            return redirect('lista_curso')
    else:
        messages.warning(
            request, 
            f'Usuário não é permitido atualizar o curso'
        )
        return redirect('home')
    

    return render(
        request,
        'curso/edita_curso.html',
        {
            'titulo':titulo,
            'form':form,
        }
    )

@login_required
def remove_curso(request, id):
    curso_obj = get_object_or_404(Curso, id=id)

    try:
        curso_obj.delete()

        messages.success(
            request, f'Curso "{curso_obj.nome_curso}" removido com sucesso'
        )
    except Exception as error:
        messages.error(
            request, f'Curso "{curso_obj.nome_curso}" não pode ser removido'
        )

    return redirect('lista_curso')


def cadastro_matricula_curso(request, id_curso):

    nome_curso = Curso.objects.get(id=id_curso).nome_curso
    titulo = f'Matricular alunos no curso {nome_curso}'
    form = MatriculaCursoForm()
    usuario_logado = request.user

    # Verifica se o User é staff
    query_user_staff = User.objects.get(id=usuario_logado.id)

    if query_user_staff.is_staff:
        if request.method == "POST":
            form = MatriculaCursoForm(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()

                messages.success(
                    request, 
                    f'Alunos matriculados com Sucesso'
                )

                return redirect('cadastro_curso')
    else:
        messages.warning(
            request, 
            f'Usuário não é permitido cadastrar curso'
        )
        return redirect('home')

    return render(
        request,
        'curso/matricula_curso.html',
        {
            'titulo':titulo,
            'form':form,
        }
    )
