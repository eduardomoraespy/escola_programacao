
from django.contrib import admin
from django.urls import path

from apps.escolar.views.home import home
from apps.escolar.views.aluno import cadastro_aluno, lista_aluno
#from apps.escolar.views.aluno import 

from apps.usuarios.views import (
    lista_usuario, cadastro_usuario, detail_usuario, edita_usuario,
    remove_usuario
)

from apps.escolar.views.professor import (
    lista_professor, cadastro_professor, detail_professor,
    edita_professor, remove_professor
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    
    # Usuário
    path('lista-usuario/', lista_usuario, name='lista_usuario'),
    path('cadastro-usuario/', cadastro_usuario, name='cadastro_usuario'),
    path('detail-usuario/<id>', detail_usuario, name='detail_usuario'),
    path('edita-usuario/<id>', edita_usuario, name='edita_usuario'),
    path('remove-usuario/<id>', remove_usuario, name='remove_usuario'),

    # Aluno 
    path('cadastro-aluno/', cadastro_aluno, name='cadastro_aluno'),

    # Professor 
    path('lista-professor/', lista_professor, name='lista_professor'),
    path('cadastro-professor/', cadastro_professor, name='cadastro_professor'),
    path('detail-professor/<id>', detail_professor, name='detail_professor'),
    path('edita-professor/<id>', edita_professor, name='edita_professor'),
    path('remove-professor/<id>', remove_professor, name='remove_professor'),

    # # Curso 
    # path('cadastro_curso/', cadastro_aluno, name='cadastro_aluno'),

]
