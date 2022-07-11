from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from accounts.forms import CadastroUsuarioForm

@login_required
def create_user(request):

    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST)
        #professor = request.POST['is_professor']
        #aluno = request.POST['is_aluno']
        #print(f'-------------------------- {professor}')
        #print(f'{aluno}----------------------------')

        print(f'--------- {form} ------------------')


        if form.is_valid():
            instance = form.save()
            professor = instance.is_professor
            print(f'-------------------------- {professor}')
            instance.set_password(instance.password)
            instance.save()

            if professor:
                print(' professor verdade')
            else:
                print('professor false')

            # if aluno:
            #     print('aluno verdade')
            # else:
            #     print('aluno  false')

            messages.success(request, 'Usuário cadastrado com sucesso.')

            return redirect('create_user')
    
    form = CadastroUsuarioForm()

    return render(
        request,
        'usuario/cadastro_usuario.html',
        {'form':form}
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