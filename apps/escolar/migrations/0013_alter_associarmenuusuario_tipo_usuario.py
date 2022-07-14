# Generated by Django 4.0.5 on 2022-07-12 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escolar', '0012_remove_associarmenuusuario_tipo_usuarioid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='associarmenuusuario',
            name='tipo_usuario',
            field=models.CharField(choices=[('P', 'Professor'), ('A', 'Aluno')], db_column='tipo_usuario', default='', max_length=194, verbose_name='Tipo de usuário: Aluno/Professor'),
        ),
    ]