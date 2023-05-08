from django.contrib import admin
#from django.contrib.admin.models import LogEntry
#from .models import CustomLogEntry

#LogEntry.__bases__ = (CustomLogEntry,)
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin ,GroupAdmin
from django.contrib.auth.models import Group
from .models import Usuarios, Departamento, Casilla, AlquilerCasillas

admin.site.unregister(Group)

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'celular', 'ci', 'departamento')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'celular', 'ci', 'departamento')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

admin.site.register(Usuarios, UserAdmin)
admin.site.register(Departamento)
admin.site.register(Casilla)
admin.site.register(AlquilerCasillas)
#admin.site.register(Usuarios.groups)
@admin.register(Group)
class CustomGroupAdmin(GroupAdmin):
    pass