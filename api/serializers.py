
from rest_framework import serializers
from .models import Usuarios, Casilla, AlquilerCasillas,Departamento,Precio
from .filters import CasillaFilter
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.response import Response
from rest_framework import filters
from datetime import timedelta
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.password_validation import validate_password
class PrecioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Precio
        fields='__all__'
class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ('nombre',)
        
class UsuariosSerializer(serializers.ModelSerializer):
    departamento = DepartamentoSerializer()
    def validate_password(self, value):
        validate_password(value)
        return make_password(value)
    class Meta:
        model = Usuarios
        fields = ['id','username','password','email','celular','ci','first_name','last_name','departamento']
    def create(self, validated_data):
        validated_data['is_superuser'] = False
        validated_data['is_staff'] = False
        validated_data['is_active'] = True
        departamento_data = validated_data.pop('departamento')
        departamento_nombre = departamento_data['nombre']
        departamentos = Departamento.objects.filter(nombre=departamento_nombre)
        if not departamentos.exists():
            raise serializers.ValidationError(f"No existe el departamento {departamento_nombre}")
        departamento = departamentos.first()
        user = Usuarios.objects.create_user(departamento=departamento,**validated_data)
        group = Group.objects.get(name='cliente') # Cambia el nombre del grupo aquí
        user.groups.add(group)

        return {
            'success': True,
            'message': 'Usuario creado exitosamente.'
        }

class NombreUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['username']
class AlqCasillasSerializer(serializers.ModelSerializer):
    departamento = DepartamentoSerializer()
    class Meta:
        model = Casilla
        fields = ['num_Casilla','departamento']

class CasillaSerializer(serializers.ModelSerializer):
    departamento = DepartamentoSerializer()
    class Meta:
        model = Casilla
        fields = '__all__'
        permission_classes = [IsAuthenticated]
        filter_backends = [DjangoFilterBackend]
        filterset_class = CasillaFilter
    def create(self, validated_data):
        departamento_data = validated_data.pop('departamento')
        departamento_nombre = departamento_data['nombre']
        departamentos = Departamento.objects.filter(nombre=departamento_nombre)
        if not departamentos.exists():
            raise serializers.ValidationError(f"No existe el departamento {departamento_nombre}")
        departamento = departamentos.first()
        num_casilla = validated_data.get('num_Casilla')
        casilla = Casilla.objects.filter(num_Casilla=num_casilla, departamento=departamento)
        if casilla.exists():
            raise serializers.ValidationError(f"Ya existe una casilla {num_casilla} en {departamento_nombre}")
        else:
            return Casilla.objects.create(departamento=departamento, **validated_data)
        return casilla

class AlquilerCasillasSerializer(serializers.ModelSerializer):
    num_casilla = serializers.IntegerField(source='fk_casilla.num_Casilla')
    departamento = serializers.CharField(source='fk_casilla.departamento.nombre')
    fecha_inicio = serializers.DateField(format="%Y-%m-%d")
    fecha_fin = serializers.DateField(format="%Y-%m-%d", required=False)
    fk_cliente = serializers.CharField()

    class Meta:
        model = AlquilerCasillas
        fields = ['id', 'num_casilla', 'departamento', 'fecha_inicio', 'fecha_fin', 'nro_contrato', 'fk_cliente']
        permission_classes = [IsAuthenticated]

    def create(self, validated_data):
        fk_casilla_data = validated_data.pop('fk_casilla')
        num_casilla = fk_casilla_data['num_Casilla']
        departamento_nombre = fk_casilla_data['departamento']['nombre']

        casilla = Casilla.objects.filter(num_Casilla=num_casilla, departamento__nombre=departamento_nombre).first()
        if not casilla:
            raise serializers.ValidationError(f"No existe la casilla {num_casilla} en el departamento {departamento_nombre}")

        if casilla.estado == "Ocupado":
            raise serializers.ValidationError(f"La casilla {num_casilla} en el departamento {departamento_nombre} está ocupada")

        casilla.estado = "Ocupado"
        casilla.save()

        fk_cliente = validated_data.pop('fk_cliente')

        usuario = Usuarios.objects.filter(username=fk_cliente, departamento=casilla.departamento).first()
        if not usuario:
            raise serializers.ValidationError(f"No existe el usuario con nombre de {fk_cliente} en el departamento {casilla.departamento}")

        alquiler_casillas = AlquilerCasillas.objects.create(fk_casilla=casilla, fk_cliente=usuario, **validated_data)
        return alquiler_casillas