# Generated by Django 4.0.5 on 2022-07-12 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escolar', '0011_tipocolaborador_alter_tipousuario_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='associarmenuusuario',
            name='tipo_usuarioID',
        ),
        migrations.AddField(
            model_name='associarmenuusuario',
            name='tipo_usuario',
            field=models.CharField(choices=[('P', 'Professor'), ('A', 'Aluno')], db_column='tipo_usuario', default=('P', 'Professor'), max_length=194, verbose_name='Tipo de usuário: Aluno/Professor'),
        ),
        migrations.DeleteModel(
            name='Tipocolaborador',
        ),
    ]