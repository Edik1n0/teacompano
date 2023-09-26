import random
from io import BytesIO
import os
from django.contrib import admin
from django.utils.text import slugify
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from PyPDF2 import PdfReader, PdfWriter  # Cambio en la importación

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
        pdf_files = []  # Lista para almacenar los archivos PDF individuales

        for kardex in queryset:
            # Generar PDF desde HTML usando WeasyPrint
            html_string = get_template('pdfs/kardex.html').render({'kardex': kardex})
            pdf_file = HTML(string=html_string).write_pdf()

            # Crear un archivo PDF temporal con el contenido de WeasyPrint
            pdf_buffer_weasy = BytesIO(pdf_file)
            pdf_files.append(pdf_buffer_weasy)

            # Crear un archivo PDF con ReportLab para la tabla de datos
            pdf_buffer_reportlab = BytesIO()
            p = canvas.Canvas(pdf_buffer_reportlab)

            # Agregar aquí tus campos y valores
            data = [
                ["Nombre del paciente", kardex.paciente],
                ["Diagnóstico", kardex.diagnosis],
                ["Dieta", kardex.dieta],
                ["Edad", kardex.edad],
                ["Peso", kardex.peso],
                ["Nivel de oxígeno", kardex.oxigeno],
                # Puedes agregar más filas según tus datos
            ]

            # Calcular el ancho de la página actual
            width, height = landscape(letter)

            # Define los anchos personalizados para cada columna en la lista colWidths
            col_widths = [200, 200]  # Ajusta los valores según tus necesidades

            table = Table(data, colWidths=col_widths)
            table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                    ('ALIGN', (0, 0), (-100, -1), 'CENTER'),
                                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                    ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

            table.wrapOn(p, width, height)
            table.drawOn(p, 80, 500)
            p.showPage()
            p.save()

            pdf_buffer_reportlab.seek(0)
            pdf_files.append(pdf_buffer_reportlab)

            # Define los anchos personalizados para cada columna en la lista colWidths
            col_widths = [50, 200]  # Ajusta los valores según tus necesidades

            table = Table(data, colWidths=col_widths)

        # Fusionar los archivos PDF generados en uno solo
        combined_pdf = BytesIO()
        pdf_writer = PdfWriter()  # Cambio en la creación del objeto PdfWriter

        for pdf_file in pdf_files:
            pdf_reader = PdfReader(pdf_file)
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

        pdf_writer.write(combined_pdf)

        # Obtener el nombre del archivo PDF
        file_name = f"{slugify(kardex.paciente)}-{kardex.fecha_kardex.strftime('%d%m%y')}.pdf"

        # Configurar la respuesta HTTP
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        response.write(combined_pdf.getvalue())

        # Cerrar los archivos PDF temporales
        for pdf_file in pdf_files:
            pdf_file.close()
        combined_pdf.close()

        return response

    generate_pdf_action.short_description = "Generar PDF de Kardex"

admin.site.register(Kardex, KardexAdmin)
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

    # Definir una función para mostrar la zona horaria en lugar de acceder a un atributo inexistente
    def get_timezone(self, obj):
        return obj.fecha_solicitud.tzinfo  # Retorna la información de zona horaria de fecha_solicitud

    get_timezone.short_description = 'Zona Horaria'  # Nombre descriptivo para el campo en el admin

admin.site.register(Formulario, FormularioAdmin)
