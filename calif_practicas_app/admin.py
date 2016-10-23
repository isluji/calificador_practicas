from django.contrib import admin

# Register your models here.
from calif_practicas_app.models import Empresa
from calif_practicas_app.models import Calificacion

#admin.site.register(Empresa)
admin.site.register(Calificacion)

# Customise the admin interface so that it automatically prepopulates
# the slug field as you type in the category name
class EmpresaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nombre',)}

# Update the registration to include this customised interface
admin.site.register(Empresa, EmpresaAdmin)
