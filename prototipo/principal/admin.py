from django.contrib import admin
from principal.models import Telefono, ModeloTelefono, Monedero, Transaccion, Dispositivo, ModeloDispositivo
# Register your models here.
class TelefonosAdministracion(admin.ModelAdmin):
    list_display = ('modelo', 'modalidad', 'imei', 'capacidad', 'color', 'proveedor', 'vendido')
    search_fields = ('proveedor', 'imei')
    
class ModeloTelefonoAdministracion(admin.ModelAdmin):
    list_display = ('nombre', 'marca')
    search_fields = ('nombre', 'marca')
    
class MonederoAdministracion(admin.ModelAdmin):
    list_display = ('nombre', 'dinero', 'fecha_actualizacion')
    search_fields = ('nombre', 'dinero')
    
class TransaccionAdministracion(admin.ModelAdmin):
    list_display = ('fecha', 'dinero')
    search_fields = ('fecha', 'dinero')

class DispositivoAdministracion(admin.ModelAdmin):
    list_display = ('modelo', 'modalidad', 'imei', 'serial', 'capacidad', 'color', 'proveedor', 'descripcion', )
    search_fields = ('proveedor', 'imei')

class ModeloDispositivoAdministracion(admin.ModelAdmin):
    list_display = ('nombre', 'marca')
    search_fields = ('nombre', 'marca')
    
admin.site.register(Telefono, TelefonosAdministracion)
admin.site.register(ModeloTelefono, ModeloTelefonoAdministracion)
admin.site.register(Monedero, MonederoAdministracion)
admin.site.register(Transaccion, TransaccionAdministracion)
admin.site.register(Dispositivo, DispositivoAdministracion)
admin.site.register(ModeloDispositivo, ModeloDispositivoAdministracion)