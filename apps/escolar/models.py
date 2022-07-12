from django.db import models


class Aluno(models.Model):

    nome = models.CharField(
        verbose_name='Nome',
        max_length=194
    )

    sobrenome = models.CharField(
        verbose_name='Sobrenome',
        max_length=194
    )

    email = models.EmailField(
        verbose_name='E-mail'
    )

    estado = models.CharField(
        verbose_name='Estado',
        max_length=2,
    ) ## Criar choice

    cidade = models.CharField(
        verbose_name='Cidade',
        max_length=50
    )

    endereco = models.CharField(
        verbose_name='Endereço',
        max_length=194
    )


    class Meta:
        verbose_name = 'aluno'
        verbose_name_plural = 'alunos'
        db_table = 'aluno'
    

    def __str__(self):
        return self.nome


class Professor(models.Model):

    nome = models.CharField(
        verbose_name='Nome',
        max_length=194
    )

    sobrenome = models.CharField(
        verbose_name='Sobrenome',
        max_length=194
    )

    email = models.EmailField(
        verbose_name='E-mail',
        unique=True
    )

    estado = models.CharField(
        verbose_name='Estado',
        max_length=2,
    ) ## Criar choice

    cidade = models.CharField(
        verbose_name='Cidade',
        max_length=50
    )

    endereco = models.CharField(
        verbose_name='Endereço',
        max_length=194
    )

    usuarioID = models.BigIntegerField(
        db_column='usuarioID',
        blank=True,
        null=True
    )



    class Meta:
        verbose_name = 'professor'
        verbose_name_plural = 'professores'
        db_table = 'professor'
    

    def __str__(self): 
        return self.nome


class TelefoneProfessor(models.Model):

    telefone = models.CharField(
        verbose_name='Telefone',
        max_length=11
    )

    professorID = models.ForeignKey(
        Professor,
        verbose_name='Professor',
        db_column='professorID',
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = 'telefone_professor'
        verbose_name_plural = 'telefones_profeesores'
        db_table = 'telefone_professor'
    

    def __str__(self):
        return self.telefone


class TelefoneAluno(models.Model):

    telefone = models.CharField(
        verbose_name='Telefone',
        max_length=11
    )

    alunoID = models.ForeignKey(
        Aluno,
        verbose_name='aluno',
        db_column='alunoID',
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = 'telefone_aluno'
        verbose_name_plural = 'telefones_alunos'
        db_table = 'telefone_aluno'
    

    def __str__(self):
        return self.telefone

class Curso(models.Model):

    nome_curso = models.CharField(
        verbose_name='Nome de Curso',
        max_length=194
    )

    ativo = models.BooleanField(
        verbose_name='Ativo'
    )

    data_inicio = models.DateField(
        verbose_name='Data de Início',
    )

    data_termino = models.DateField(
        verbose_name='Data de Término',
    )

    professorID = models.ForeignKey(
        Professor,
        verbose_name='Professor',
        db_column='professorID',
        on_delete=models.PROTECT
    )


    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'
        db_table = 'curso'
    

    def __str__(self):
        return self.nome_curso


class LkeDeslike(models.Model):

    cursoID = models.ForeignKey(
        Curso,
        verbose_name='Curso',
        db_column='cursoID',
        on_delete=models.PROTECT
    )

    alunoID = models.ForeignKey(
        Aluno,
        verbose_name='Aluno',
        db_column='alunoID',
        on_delete=models.PROTECT
    )

    like = models.PositiveIntegerField(
        verbose_name='Like',
    )

    deslike = models.PositiveIntegerField(
        verbose_name='DesLike',
    )


    class Meta:
        verbose_name = 'likedeslike'
        verbose_name_plural = 'likedeslikes'
        db_table = 'likedeslike'



class TipoUsuario(models.Model):

    tipo_usuario = models.CharField(
        verbose_name='Tipo de Usuário',
        max_length=194
    )

    is_professor = models.BooleanField(
        default=False,
    )

    is_aluno = models.BooleanField(
        default=False,
    )

    usuarioID =  models.IntegerField(
        db_column='usuarioID',
        default=0
    )
    class Meta:
        verbose_name = 'tipo_usuario'
        verbose_name_plural = 'tipos_usuarios'
        db_table = 'tipo_usuario'
    
    def __str__(self):
        return self.tipo_usuario


class Menu(models.Model):

    nome_menu = models.CharField(
        verbose_name='Opção visível no menu',
        max_length=50
    )

    caminho = models.CharField(
        verbose_name='Caminho',
        max_length=194
    )

    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menus'
        db_table = 'menu'
    
    def __str__(self):
        return self.nome_menu


class AssociarMenuUsuario(models.Model):

    tipo_usuarioID = models.ForeignKey(
        TipoUsuario,
        verbose_name='Tipo de usuário: Aluno/Professor',
        db_column='tipo_usuarioID',
        on_delete=models.PROTECT
    )

    menuID = models.ForeignKey(
        Menu,
        verbose_name='Opção visível no menu',
        db_column='menuID',
        on_delete=models.PROTECT,
        default=0
    )

    is_staff = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'associar_menu_usuario'
        verbose_name_plural = 'associar_menu_usuarios'
        db_table = 'associar_menu_usuario'