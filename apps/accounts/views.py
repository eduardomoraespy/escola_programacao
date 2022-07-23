from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator

from accounts.forms import CadastroUsuarioForm, DetailUsuarioForm, EditaUsuarioForm
from escolar.models import TipoUsuario
from django.contrib.auth.models import User

@login_required
def lista_usuario(request):

    titulo = 'Lista de Usuários'
    query_usuario = User.objects.filter(is_active=True)
    paginator = Paginator(query_usuario, 5)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    return render(
        request,
        'usuario/lista_usuario.html',
        {
            'titulo':titulo,
            'query_usuario':query_usuario,
            'page_obj': page_obj
        }
    )

@login_required
def cadastro_usuario(request):

    titulo = 'Cadastro Usuário'

    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        form.data._mutable = True

        if form.is_valid():
            instance = form.save(commit=False)
            instance.set_password(instance.password)
            instance.save()

            try:
                professor = form.data['is_professor']

                TipoUsuario.objects.create(
                    tipo_usuario='Professor',
                    is_professor=True,
                    usuarioID = instance.id
                )

            except:
                pass

            try:
                aluno = form.data['is_aluno']

                TipoUsuario.objects.create(
                    tipo_usuario='Aluno',
                    is_aluno=True,
                    usuarioID = instance.id
                )

            except:
                pass

            messages.success(request, f'Usuário "{instance.first_name}" cadastrado com sucesso.')

            return redirect('cadastro_usuario')
    
    form = CadastroUsuarioForm()

    return render(
        request,
        'usuario/cadastro_usuario.html',
        {
            'titulo':titulo,
            'form':form
        }
    )

def detail_usuario(request, id):

    titulo = 'Detalhes do Usuário'
    usuario_obj = get_object_or_404(User, id=id)
    form = DetailUsuarioForm(instance=usuario_obj)

    return render(
        request,
        'usuario/detail_usuario.html',
        {
            'titulo':titulo,
            'form':form
        }
    )

@login_required
def edita_usuario(request, id):
    
    titulo = 'Editar Usuário'

    usuario_obj = get_object_or_404(User, id=id)
    form = EditaUsuarioForm(request.POST, instance=usuario_obj)

    form.data._mutable = True

    if form.is_valid():
        instance = form.save(commit=False)
        instance.set_password(instance.password)
        instance.save()

        try:
            professor = form.data['is_professor']

            TipoUsuario.objects.create(
                tipo_usuario='Professor',
                is_professor=True,
                usuarioID = instance.id
            )

        except:
            pass

        try:
            aluno = form.data['is_aluno']

            TipoUsuario.objects.create(
                tipo_usuario='Aluno',
                is_aluno=True,
                usuarioID = instance.id
            )

        except:
            pass

        messages.success(request, 'Usuário atualizado com sucesso.')

        return redirect('lista_usuario')

    return render(
        request,
        'usuario/edita_usuario.html',
        {
            'titulo':titulo,
            'form':form
        }
    )

def user_login(request): ## login usuario
    template_name = 'login.html'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') # Usuario logado
        else:
            print('Erro no login')

    return render(request, template_name, {})

@login_required(login_url='/login/')
def user_profile(request): ## função para usuario ja logado
    template_name = 'home.html'
    return render(request, template_name, {})


@login_required(login_url='/login/')
def user_logout(request): # logout e redireciona para página login
    logout(request)
    messages.success(request, 'Você saiu do sistema.')
    return redirect('user_login')