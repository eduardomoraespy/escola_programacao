
#from django.contrib import admin
from django.urls import path

from apps.escolar.views.home import home, form_base
from apps.escolar.views.aluno import cadastro_aluno, lista_aluno

urlpatterns = [
    #path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('form_base/', form_base, name='form_base'),
    path('lista-aluno/', lista_aluno, name='lista_aluno'),
    path('cadastro_aluno/', cadastro_aluno, name='cadastro_aluno'),

]
