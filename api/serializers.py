
from rest_framework import serializers
from .models import Usuarios, Casilla, AlquilerCasillas,Departamento
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group

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
class UsuariosAlquilerSerializer():
    class Meta:
        model = Usuarios
        fields=['id','username']
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
    fk_casilla=CasillaSerializer()
    fk_cliente=UsuariosAlquilerSerializer()
    class Meta:
        model = AlquilerCasillas
        fields = ['id','fk_casilla','fecha_inicio','fecha_fin','nro_contrato','fk_cliente']


