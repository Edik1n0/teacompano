import random
from io import BytesIO
from django.contrib import admin
from django.core.files.base import ContentFile
from django.utils import timezone
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from django.utils.text import slugify
from django.http import HttpResponse
from django.urls import reverse
from django.utils.html import format_html
from django.template.loader import get_template
from weasyprint import HTML  # Importa WeasyPrint

from .models import Kardex, Asesor, Formulario, Video, Pagina, Service, Galeria

class KardexAdmin(admin.ModelAdmin):
    list_display = (
        'paciente',
        'fecha_kardex',
        'diagnosis',
        'dieta',
        'edad',
        'peso',
        'oxigeno',
    )
    actions = ['generate_pdf_action']

    def generate_pdf_action(self, request, queryset):
        pdf_buffer = BytesIO()

        for kardex in queryset:
            # Crear un documento PDF utilizando ReportLab
            pdf_document = SimpleDocTemplate(pdf_buffer)

            # Crear una lista de elementos para agregar al PDF
            elements = []

            # Crear imagen de fondo
            background_image_path = "web/static/img/plantilla-kardex.jpg"
            image = Image(background_image_path)

            # Crear la tabla con los datos y aplicar los estilos
            table_data = [
                ['Nombre del paciente', kardex.paciente],
                ['Diagnóstico', kardex.diagnosis],
                ['Dieta', kardex.dieta],
                ['Edad', kardex.edad],
                ['Peso', kardex.peso],
                ['Tratamiento', kardex.tratamiento],
                ['Plan', kardex.plan],
                ['Fecha de creación', kardex.fecha_kardex.strftime('%Y-%m-%d %H:%M:%S')],
            ]

            table_style = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ])

            # Crear la tabla con los datos y aplicar los estilos
            table = Table(table_data, colWidths=[430, 556])  # Ajusta los valores según tus necesidades
            table.setStyle(table_style)

            # Agregar la imagen de fondo y la tabla al PDF
            elements.append(image)
            elements.append(Spacer(1, 10))  # Espacio en blanco para separar
            elements.append(table)

            # Construir el documento PDF
            pdf_document.build(elements)

        # Generar un nombre de archivo usando el nombre del paciente y la fecha de creación
        file_name = f"{slugify(kardex.paciente)}-{kardex.fecha_kardex.strftime('%d%m%y')}.pdf"
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'

        # Configurar la respuesta HTTP
        response.write(pdf_buffer.getvalue())
        pdf_buffer.close()

        return response

    generate_pdf_action.short_description = "Generar PDF de Kardex"

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

    def get_timezone(self, obj):
        return obj.fecha_solicitud.timezone  # Retorna el valor de timezone de la fecha_solicitud

    #get_timezone.short_description = 'Timezone'  # Nombre descriptivo para el campo en el admin

admin.site.register(Formulario, FormularioAdmin)
