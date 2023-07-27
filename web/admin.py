from django.contrib import admin
from .models import Asesor, Pagina, Video, Formulario

# Register your models here.
admin.site.register(Asesor)
admin.site.register(Pagina)
admin.site.register(Video)

class FormularioAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_solicitud', 'get_timezone')

    def get_timezone(self, obj):
        return obj.fecha_solicitud.timezone  # Retorna el valor de timezone de la fecha_solicitud

    get_timezone.short_description = 'Timezone'  # Nombre descriptivo para el campo en el admin

admin.site.register(Formulario, FormularioAdmin)
