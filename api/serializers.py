
from rest_framework import serializers
from .models import Usuarios, Casilla, AlquilerCasillas,Departamento
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group

from datetime import timedelta

from django.contrib.auth.password_validation import validate_password
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
        fields='__all__'
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
        return user

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
    fk_casilla=AlqCasillasSerializer()
    fk_cliente=NombreUsuarioSerializer()
    class Meta:
        model = AlquilerCasillas
        fields = ['id','fk_casilla','fecha_inicio','fecha_fin','nro_contrato','fk_cliente']
    def create(self, validated_data):
        username_data = validated_data.pop('fk_cliente')
        username = username_data['username']

        try:
            usuario = Usuarios.objects.get(username=username)
            raise serializers.ValidationError("Ya existe este usuario")
        except Usuarios.DoesNotExist:
            usuario = Usuarios.objects.create(username=username)  # Crear el usuario si no existe

        casilla_data = validated_data.pop('fk_casilla')
        departamento_data = casilla_data['departamento']
        departamento_nombre = departamento_data['nombre']
        num_casilla = casilla_data['num_Casilla']

        departamentos = Departamento.objects.filter(nombre=departamento_nombre)
        if not departamentos.exists():
            raise serializers.ValidationError(f"No existe el departamento {departamento_nombre}")

        departamento = departamentos.first()

        casillas = Casilla.objects.filter(num_Casilla=num_casilla, departamento=departamento)
        if not casillas.exists():
            raise serializers.ValidationError(f"No existe la casilla {num_casilla} en el departamento {departamento_nombre}")

        validated_data['fk_cliente'] = usuario
        validated_data['fk_casilla'] = casillas.first()

        return super().create(validated_data)