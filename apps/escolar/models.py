from django.db import models

class Telefone(models.Model):

    telefone = models.CharField(
        verbose_name='Telefone',
        max_length=11
    )

    class Meta:
        verbose_name = 'telefone'
        verbose_name_plural = 'telefones'
        db_table = 'telefone'
    

    def __str__(self):
        return self.telefone


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


    telefoneID = models.ForeignKey(
        Telefone,
        verbose_name='Telefone',
        db_column='telefoneID',
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )


    # # tratando campo vazio ou null
    # def get_horario_saida(self):
    #     if self.horario_saida:
    #         return self.horario_saida
        
    #     return 'Horário de saída não registrado'

    # def get_horario_autorizacao(self):
    #     if self.horario_autorizacao:
    #         return self.horario_autorizacao
        
    #     return 'Visitante aguardando autorização'
    
    # def get_morador_resposavel(self):
    #     if self.morador_resposavel:
    #         return self.morador_resposavel
        
    #     return 'Visitante aguardando autorização'
    
    # def get_placa_veiculo(self):
    #     if self.placa_veiculo:
    #         return self.placa_veiculo
        
    #     return 'Veículo não registrado'

    # def get_cpf(self):
    #     if self.cpf:
    #         cpf = str(self.cpf)

    #         cpf_parte_um = cpf[0:3]
    #         cpf_parte_dois = cpf[3:6]
    #         cpf_parte_tres = cpf[6:9]
    #         cpf_parte_quatro = cpf[9:]

    #         cpf_formatado = f'{cpf_parte_um}.{cpf_parte_dois}.{cpf_parte_tres}-{cpf_parte_quatro}'

    #         return cpf_formatado

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

    # telefones = models.CharField(
    #     verbose_name='Telefones',
    #     max_length=11
    # ) # deve permitir cadastrar mais de um telefone (criar tabela com telefones e relacionar com aluno)

    telefoneID = models.ForeignKey(
        Telefone,
        verbose_name='Telefone',
        db_column='telefoneID',
        on_delete=models.PROTECT
    )


    class Meta:
        verbose_name = 'professor'
        verbose_name_plural = 'professores'
        db_table = 'professor'
    

    def __str__(self): 
        return self.nome


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


class Menu(models.Model):

    nome_menu = models.CharField(
        verbose_name='Opção visível no menu',
        max_length=50
    )

    caminho = models.CharField(
        verbose_name='Caminho',
        max_length=194
    )

    # usuarioID = models.ForeignKey(
    #     Usuario,
    #     verbose_name='usuario logado',
    #     db_column='usuarioID',
    #     on_delete=models.PROTECT
    # )

    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menus'
        db_table = 'menu'

