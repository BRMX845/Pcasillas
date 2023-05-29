from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission
# Create your models here.
from django.db import models
class Departamento(models.Model):
    nombre = models.CharField(max_length=100, null=False)

class Usuarios(AbstractUser):
    celular = models.IntegerField()
    ci=models.IntegerField(unique=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='api_usuarios_groups',  # nombre de related_name único
        blank=True,
        verbose_name='grupos'
    )

    # relacion ManyToMany con la tabla auth.Permission
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='api_usuarios_permissions_set',  # nombre de related_name único
        blank=True,
        verbose_name='permisos del usuario'
    )

class Casilla(models.Model):
    num_Casilla=models.IntegerField(default=0)
    tamaño = models.CharField(max_length=10, null=False)
    estado = models.CharField(max_length=20, null=False)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

class Precio(models.Model):
    casilla = models.ForeignKey(Casilla, on_delete=models.CASCADE)
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    precio_semanal = models.DecimalField(max_digits=10, decimal_places=2)
    precio_anual = models.DecimalField(max_digits=10, decimal_places=2)

class AlquilerCasillas(models.Model):
    fk_cliente = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    fk_casilla = models.ForeignKey(Casilla, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True)
    nro_contrato = models.CharField(max_length=20, unique=True)
    TIPO_ALQUILER_CHOICES = [
        ('M', 'Mensual'),
        ('S', 'Semanal'),
        ('A', 'Anual'),
    ]
    tipo_alquiler = models.CharField(max_length=1, choices=TIPO_ALQUILER_CHOICES, default='S ')  # Valor predeterminado 'M' para mensual

