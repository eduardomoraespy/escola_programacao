from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from escolar.models import *
from django.contrib.auth.models import User
from escolar.forms.cadastro_opcoes_menu import CadastroMenuForm, DetailMenuForm, EditaMenuForm

@login_required
def lista_menu(request):

    titulo = 'Lista Menu'
    query_menu = Menu.objects.all()
    paginator = Paginator(query_menu, 5)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    usuario_logado = request.user
    query_superuser = User.objects.get(id=usuario_logado.id)

    # Apenas superusuario pode cadastrar e gerênciar menu
    if query_superuser.is_superuser:
        return render(
            request,
            'menu/lista_menu.html',
            {
                'titulo':titulo,
                'query_menu':query_menu,
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
def cadastro_menu(request):

    titulo = 'Cadastro Menu'
    form = CadastroMenuForm()
    usuario_logado = request.user
    query_superuser = User.objects.get(id=usuario_logado.id)

    # Apenas superusuario pode cadastrar e gerênciar menu
    if query_superuser.is_superuser:
        if request.method == "POST":
            form = CadastroMenuForm(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()

                messages.success(
                    request, 
                    f'Menu: {instance.nome_menu} registrado com Sucesso'
                )

                return redirect('cadastro_menu')
    else:
        messages.warning(
            request, 
            f'Usuário não é permitido cadastrar Menu'
        )
        return redirect('home')

    return render(
        request,
        'menu/cadastro_menu.html',
        {
            'titulo':titulo,
            'form':form,
        }
    )

@login_required
def detail_menu(request, id):

    titulo = 'Detalhes do Menu'
    menu_obj = get_object_or_404(Menu, id=id)
    form = DetailMenuForm(instance=menu_obj)
    usuario_logado = request.user
    query_superuser = User.objects.get(id=usuario_logado.id)

    # Apenas superusuario pode cadastrar e gerênciar menu
    if query_superuser.is_superuser:
        return render(
            request,
            'menu/detail_menu.html',
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
def edita_menu(request, id):

    titulo = 'Editar Menu'
    menu_obj = get_object_or_404(Menu, id=id)
    form = EditaMenuForm(request.POST or None, instance=menu_obj)
    usuario_logado = request.user
    query_superuser = User.objects.get(id=usuario_logado.id)

    # Apenas superusuario pode cadastrar e gerênciar menu
    if query_superuser.is_superuser:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            messages.success(
                request, f'Menu: {instance.nome_menu} atualizado com Sucesso'
            )

            return redirect('lista_menu')
    else:
        messages.warning(
            request, 
            f'Usuário não é permitido atualizar menu'
        )
        return redirect('home')
    

    return render(
        request,
        'menu/edita_menu.html',
        {
            'titulo':titulo,
            'form':form,
        }
    )

@login_required
def remove_menu(request, id):
    menu_obj = get_object_or_404(Menu, id=id)

    try:
        menu_obj.delete()

        messages.success(
            request, f'Menu: "{menu_obj.nome_menu}" removido com sucesso'
        )
    except Exception as error:
        messages.error(
            request, f'Menu: "{menu_obj.nome_menu}" não pode ser removido'
        )

    return redirect('lista_menu')