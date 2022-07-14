# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class VwMenuUsuario(models.Model):
    tipo_usuario = models.CharField(max_length=194, blank=True, null=True)
    usuario_id = models.IntegerField(blank=True, null=True)
    menu_id = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    caminho = models.CharField(max_length=194, blank=True, null=True)
    nome_menu = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'vw_menu_usuario'
