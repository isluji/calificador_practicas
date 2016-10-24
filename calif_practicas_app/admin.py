"Registro de modelos en la interfaz de administrador"


from django.contrib import admin

# Register your models here.
from calif_practicas_app.models import Empresa
from calif_practicas_app.models import Calificacion

# Customise the admin interface so that it automatically prepopulates
# the slug field as you type in the enterprise name
class EmpresaAdmin(admin.ModelAdmin):
    """
    Interfaz de administrador personalizada para el modelo Empresa,
    anadiendo la funcionalidad de que, cuando creamos una nueva Empresa
    a traves de dicha interfaz, se actualice automaticamente el "slug"
    conforme escribimos el nombre de la empresa.
    """
    prepopulated_fields = {'slug':('nombre',)}

# Update the registration to include this customised interface
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Calificacion)
