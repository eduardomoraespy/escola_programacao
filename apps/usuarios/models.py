from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, 
    AbstractBaseUser,
    PermissionsMixin
)


class UsuarioManager(BaseUserManager):

    def create_user(self, email, password=None):
        usuario = self.model(
            email = self.normalize_email(email)
        )

        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False

        if password:
            usuario.set_password(password)
        
        usuario.save()

        return usuario
    
    def create_superuser(self, email, password):
        usuario = self.create_user(
            email = self.normalize_email(email),
            password = password
        )

        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True

        usuario.set_password(password)
        
        usuario.save()

        return usuario

class Usuario(AbstractBaseUser, PermissionsMixin):

    nome_login = models.CharField(
        max_length=255, 
        blank=True, 
        null=True
    )

    email = models.EmailField(
        verbose_name='Email do Usuário',
        max_length=194,
        unique=True
    )

    password = models.CharField(max_length=255)

    # campos para modelo personalizado de usuários
    is_active = models.BooleanField(
        verbose_name='Usuário está ativo',
        default=True
    )

    is_staff = models.BooleanField(
        verbose_name='Usuário gerênciador',
        default=False
    )

    is_superuser = models.BooleanField(
        verbose_name='Usuário é um Super Usuário',
        default=False
    )

    USERNAME_FIELD = 'email'

    objects = UsuarioManager()

    class Meta:
        managed = False
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
        db_table = 'usuario'

    def __str__(self):
        return self.email