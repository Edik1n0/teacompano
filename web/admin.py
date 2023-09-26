import random
import os
import tempfile
from django.utils.text import slugify
from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from django.utils.html import format_html
from django.template.loader import get_template
from weasyprint import HTML, CSS

from .models import Kardex, Asesor, Formulario, Video, Pagina, Service, Galeria, ImagenesPrincipales

class KardexAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'fecha_kardex', 'edad', 'oxigeno')
    search_fields = ('paciente', 'diagnosis', 'dieta', 'oxigeno', 'edad', 'peso')
    list_filter = ('fecha_kardex',)

    actions = ['generate_pdf']

    def generate_pdf(self, request, queryset):
        # Configurar el tamaño de página adecuado (A4 en este ejemplo)
        page_size = 'A4'
        
        # Crear una respuesta HTTP para el PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="kardex.pdf"'

        # Crear un directorio temporal para archivos temporales
        temp_dir = tempfile.mkdtemp()

        for kardex in queryset:
            # Crear el contenido HTML directamente en el código
            html_content = f"""
                <html>
                    <head>
                        <title>Kardex</title>
                        <style>
                            @page {{
                                size: {page_size};
                                margin: 1cm;
                            }}
                        </style>
                    </head>
                    <body>
                        <h1>Kardex de {kardex.paciente}</h1>
                        <p>Fecha: {kardex.fecha_kardex}</p>
                        <p>Edad: {kardex.edad}</p>
                        <p>Oxígeno: {kardex.oxigeno}</p>
                        <!-- Agrega aquí más contenido según tus necesidades -->
                    </body>
                </html>
            """

            # Obtener el nombre del archivo PDF basado en el nombre del paciente y la fecha
            file_name = f"{slugify(kardex.paciente)}_{kardex.fecha_kardex.strftime('%d%m%y')}.pdf"
            pdf_file_path = os.path.join(temp_dir, file_name)

            # Generar el PDF utilizando WeasyPrint
            HTML(string=html_content).write_pdf(pdf_file_path, stylesheets=[CSS(string='@page { size: A4; margin: 1cm; }')])

            # Adjuntar el PDF generado a la respuesta HTTP
            with open(pdf_file_path, 'rb') as pdf_file:
                response.write(pdf_file.read())

        # Eliminar archivos temporales y el directorio temporal
        for temp_file in os.listdir(temp_dir):
            temp_file_path = os.path.join(temp_dir, temp_file)
            os.remove(temp_file_path)
        os.rmdir(temp_dir)

        return response

    generate_pdf.short_description = 'Generar PDF kardex'

# Registrar el modelo Kardex con la clase de administración personalizada
admin.site.register(Kardex, KardexAdmin)
admin.site.register(Asesor)
admin.site.register(Pagina)
admin.site.register(Video)

class GaleriaAdmin(admin.ModelAdmin):
    list_display = (
        'identificador',
    )

admin.site.register(Galeria, GaleriaAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('servicename', 'asesor', 'serviceupdated')

admin.site.register(Service, ServiceAdmin)

class FormularioAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_solicitud', 'servicio')

admin.site.register(Formulario, FormularioAdmin)

class ImagenesPrincipalesAdmin(admin.ModelAdmin):
    list_display = ('imgname', 'imagenalt', 'imgasesor')

admin.site.register(ImagenesPrincipales, ImagenesPrincipalesAdmin)