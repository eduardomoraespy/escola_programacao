from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from escolar.models import *
from django.contrib.auth.models import User
from escolar.forms.professor import CadastroProfessorForm, DetailProfessorForm, EditaProfessorForm

@login_required
def lista_professor(request):

    titulo = 'Lista de Professores'
    query_professor = Professor.objects.all()
    paginator = Paginator(query_professor, 5)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    usuario_logado = request.user
    query_user_staff = User.objects.get(id=usuario_logado.id)

    return render(
        request,
        'professor/lista_professor.html',
        {
            'titulo':titulo,
            'query_professor':query_professor,
            'query_user_staff':query_user_staff,
            'page_obj': page_obj
        }
    )

@login_required
def cadastro_professor(request):

    titulo = 'Cadastro de Professor'
    form = CadastroProfessorForm()
    usuario_logado = request.user

    # Verifica se o User é staff
    query_user_staff = User.objects.get(id=usuario_logado.id)

    if query_user_staff.is_staff:
        if request.method == "POST":
            form = CadastroProfessorForm(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.usuarioID = usuario_logado
                instance.save()

                messages.success(
                    request, 
                    f'Professor {instance.nome} registrado com Sucesso'
                )

                return redirect('cadastro_professor')
    else:
        messages.warning(
            request, 
            f'Usuário não é permitido cadastrar professor'
        )
        return redirect('home')

    return render(
        request,
        'professor/cadastro_professor.html',
        {
            'titulo':titulo,
            'form':form,
        }
    )

@login_required
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

@login_required
def edita_professor(request, id):

    titulo = 'Editar Professor'
    professor_obj = get_object_or_404(Professor, id=id)
    form = EditaProfessorForm(request.POST or None, instance=professor_obj)
    usuario_logado = request.user

    # Verifica se o User é staff
    query_user_staff = User.objects.get(id=usuario_logado.id)

    if query_user_staff.is_staff:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.usuarioID = usuario_logado.id
            instance.save()

            messages.success(
                request, f'Professor {instance.nome} atualizado com Sucesso'
            )

            return redirect('lista_professor')
    else:
        messages.warning(
            request, 
            f'Usuário não é permitido atualizar professor'
        )
        return redirect('home')
    

    return render(
        request,
        'professor/edita_professor.html',
        {
            'titulo':titulo,
            'form':form,
        }
    )

@login_required
def remove_professor(request, id):
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