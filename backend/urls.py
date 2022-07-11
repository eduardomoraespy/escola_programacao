
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from apps.escolar.views.home import home
from apps.escolar.views.menu import menu

# from apps.usuarios.views import (
#     lista_usuario, cadastro_usuario, detail_usuario, edita_usuario,
#     remove_usuario
# )

from apps.accounts.views import *

from apps.escolar.views.professor import (
    lista_professor, cadastro_professor, detail_professor,
    edita_professor, remove_professor
)

from apps.escolar.views.aluno import (
    lista_aluno, cadastro_aluno, detail_aluno, edita_aluno,
    remove_aluno
)

from apps.accounts.aoi_accounts.usuario_logado import UsuarioLogadoViewSet

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),

    path('', home, name='home'),
    path('menu/', menu, name='menu'),

    path('cadastro-usuario/', create_user, name='create_user'),
    
    # Usuário
    # path('lista-usuario/', lista_usuario, name='lista_usuario'),
    # path('cadastro-usuario/', cadastro_usuario, name='cadastro_usuario'),
    # path('detail-usuario/<id>', detail_usuario, name='detail_usuario'),
    # path('edita-usuario/<id>', edita_usuario, name='edita_usuario'),
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
    # path('cadastro_curso/', cadastro_aluno, name='cadastro_aluno'),


    # ----------- API --------------

    # Usuário
    path('usuario-logado/', UsuarioLogadoViewSet.as_view(actions={"get": "get_usuario_logado"}),name="get_usuario_logado"),

]
