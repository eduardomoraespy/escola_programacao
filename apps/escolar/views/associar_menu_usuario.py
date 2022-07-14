from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from escolar.models import *
from django.contrib.auth.models import User
from escolar.forms.associar_menu_usuario import AssociarMenuForm, DetailAssociarMenuUsuarioForm, EditaAssociarMenuUsuarioForm

@login_required
def lista_menu_associar(request):

    titulo = 'Lista Menu Associado à um usuário'
    query_menu_associado = AssociarMenuUsuario.objects.all()
    paginator = Paginator(query_menu_associado, 5)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    usuario_logado = request.user
    query_superuser = User.objects.get(id=usuario_logado.id)

    # Apenas superusuario pode cadastrar e gerênciar menu
    if query_superuser.is_superuser:
        return render(
            request,
            'menu_associar/lista_menu_associar.html',
            {
                'titulo':titulo,
                'query_menu':query_menu_associado,
                'query_superuser':query_superuser,
                'page_obj': page_obj
            }
        )
    
    else:
        messages.warning(
            request, 
            f'Usuário não é permitido visualizar menu como opcão'
        )
        return redirect('home')

@login_required
def cadastro_menu_associar(request):

    titulo = 'Associar Menu ao usário'
    form = AssociarMenuForm()
    usuario_logado = request.user
    query_superuser = User.objects.get(id=usuario_logado.id)

    # Apenas superusuario pode cadastrar e gerênciar menu
    if query_superuser.is_superuser:
        if request.method == "POST":
            form = AssociarMenuForm(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                if query_superuser.is_staff:
                    instance.is_staff = usuario_logado.is_staff
                instance.save()

                messages.success(
                    request, 
                    f'Menu: {instance.menuID} registrado com Sucesso'
                )

                return redirect('cadastro_menu_associar')
    else:
        messages.warning(
            request, 
            f'Usuário não é permitido associar Menu'
        )
        return redirect('home')

    return render(
        request,
        'menu_associar/cadastro_menu_associar.html',
        {
            'titulo':titulo,
            'form':form,
        }
    )

@login_required
def detail_menu_associar(request, id):

    titulo = 'Detalhes do Usuário associado ao menu'
    menu_assocido_obj = get_object_or_404(AssociarMenuUsuario, id=id)
    form = DetailAssociarMenuUsuarioForm(instance=menu_assocido_obj)
    usuario_logado = request.user
    query_superuser = User.objects.get(id=usuario_logado.id)

    # Apenas superusuario pode cadastrar e gerênciar menu
    if query_superuser.is_superuser:
        return render(
            request,
            'menu_associar/detail_menu_associar.html',
            {
                'titulo':titulo,
                'form':form
            }
        )
    else:
        messages.warning(
            request, 
            f'Usuário não é permitido visualizar menu como opcão'
        )
        return redirect('home')

@login_required
def edita_menu_associar(request, id):

    titulo = 'Editar menu Associado ao usuário'
    menu_associado_obj = get_object_or_404(AssociarMenuUsuario, id=id)
    form = EditaAssociarMenuUsuarioForm(request.POST or None, instance=menu_associado_obj)
    usuario_logado = request.user
    query_superuser = User.objects.get(id=usuario_logado.id)

    # Apenas superusuario pode cadastrar e gerênciar menu
    if query_superuser.is_superuser:
        if form.is_valid():
            instance = form.save(commit=False)
            if query_superuser.is_staff:
                instance.is_staff = usuario_logado.is_staff
            instance.save()

            messages.success(
                request, f'Associação: "{instance.menuID}" atualizado com Sucesso'
            )

            return redirect('lista_menu_associar')
    else:
        messages.warning(
            request, 
            f'Usuário não é permitido atualizar associação ao menu'
        )
        return redirect('home')
    

    return render(
        request,
        'menu_associar/edita_menu_associar.html',
        {
            'titulo':titulo,
            'form':form,
        }
    )

@login_required
def remove_menu_associar(request, id):
    menu_associado_obj = get_object_or_404(AssociarMenuUsuario, id=id)

    try:
        menu_associado_obj.delete()

        messages.success(
            request, f'Menu: "{menu_associado_obj.menuID}" removido com sucesso'
        )
    except Exception as error:
        messages.error(
            request, f'Menu: "{menu_associado_obj.menuID}" não pode ser removido'
        )

    return redirect('lista_menu_associar')