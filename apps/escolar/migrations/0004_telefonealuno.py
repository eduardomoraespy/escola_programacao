# Generated by Django 4.0.5 on 2022-07-08 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escolar', '0003_telefoneprofessor_remove_aluno_telefoneid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelefoneAluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone')),
                ('alunoID', models.ForeignKey(db_column='alunoID', on_delete=django.db.models.deletion.PROTECT, to='escolar.aluno', verbose_name='aluno')),
            ],
            options={
                'verbose_name': 'telefone_aluno',
                'verbose_name_plural': 'telefones_alunos',
                'db_table': 'telefone_aluno',
            },
        ),
    ]