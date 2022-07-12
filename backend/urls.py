
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from apps.escolar.views.home import *
from apps.accounts.views import *
from apps.escolar.views.professor import *
from apps.escolar.views.aluno import *
from apps.escolar.views.cadastro_opcoes_menu import *
from apps.escolar.views.associar_menu_usuario import *

from apps.accounts.api_accounts.usuario_logado import UsuarioLogadoViewSet

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),

    # Home
    path('', home, name='home'),

    # Usuário
    path('lista-usuario/', lista_usuario, name='lista_usuario'),
    path('cadastro-usuario/', cadastro_usuario, name='cadastro_usuario'),
    path('detail-usuario/<id>', detail_usuario, name='detail_usuario'),
    path('edita-usuario/<id>', edita_usuario, name='edita_usuario'),
    # path('remove-usuario/<id>', remove_usuario, name='remove_usuario'),

    # Aluno 
    path('lista-aluno/', lista_aluno, name='lista_aluno'),
    path('cadastro-aluno/', cadastro_aluno, name='cadastro_aluno'),
    path('detail-aluno/<id>', detail_aluno, name='detail_aluno'),
    path('edita-aluno/<id>', edita_aluno, name='edita_aluno'),
    path('remove-aluno/<id>', remove_aluno, name='remove_aluno'),

    # Professor 
    path('lista-professor/', lista_professor, name='lista_professor'),
    path('cadastro-professor/', cadastro_professor, name='cadastro_professor'),
    path('detail-professor/<id>', detail_professor, name='detail_professor'),
    path('edita-professor/<id>', edita_professor, name='edita_professor'),
    path('remove-professor/<id>', remove_professor, name='remove_professor'),

    # # Curso 
    # path('cadastro-curso/', cadastro_curso, name='cadastro_curso'),

    # Menu
    path('lista-menu/', lista_menu, name='lista_menu'),
    path('cadastro-menu/', cadastro_menu, name='cadastro_menu'),
    path('detail-menu/<id>', detail_menu, name='detail_menu'),
    path('edita-menu/<id>', edita_menu, name='edita_menu'),
    path('remove-menu/<id>', remove_menu, name='remove_menu'),

    # permissões menu
    path('lista-menu-associar/', lista_menu_associar, name='lista_menu_associar'),
    path('cadastro-menu-associar/', cadastro_menu_associar, name='cadastro_menu_associar'),
    path('detail-menu-associar/<id>', detail_menu_associar, name='detail_menu_associar'),
    path('edita-menu-associar/<id>', edita_menu_associar, name='edita_menu_associar'),
    path('remove-menu-associar/<id>', remove_menu_associar, name='remove_menu_associar'),


    # ----------- API --------------

    # Usuário
    path('usuario-logado/', UsuarioLogadoViewSet.as_view(actions={"get": "get_usuario_logado"}),name="get_usuario_logado"),

]
