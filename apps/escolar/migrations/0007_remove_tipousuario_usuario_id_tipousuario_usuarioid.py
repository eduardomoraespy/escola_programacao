# Generated by Django 4.0.5 on 2022-07-11 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escolar', '0006_tipousuario_usuario_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipousuario',
            name='usuario_id',
        ),
        migrations.AddField(
            model_name='tipousuario',
            name='usuarioID',
            field=models.IntegerField(db_column='usuarioID', default=0),
        ),
    ]
