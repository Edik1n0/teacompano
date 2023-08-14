from django.contrib import admin
from reportlab.platypus import SimpleDocTemplate, Image, PageBreak
from reportlab.lib.pagesizes import letter, landscape
from io import BytesIO
from django.utils.text import slugify
from django.http import HttpResponse
from django.urls import reverse
from django.utils.html import format_html

from .models import Kardex

class KardexAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'fecha_kardex', 'diagnosis', 'dieta', 'edad', 'peso', 'generate_pdf_link')
    actions = ['generate_pdf_action']

    def generate_pdf_link(self, obj):
        pdf_url = reverse('generate_pdf', args=[obj.id])
        return format_html('<a href="{}">Generar PDF</a>', pdf_url)
    
    generate_pdf_link.short_description = "PDF"

    def generate_pdf_action(self, request, queryset):
        pdf_buffer = BytesIO()
        doc = SimpleDocTemplate(pdf_buffer, pagesize=landscape(letter))

        content = []

        for kardex in queryset:
            # Crear una lista para el contenido de la página
            page_content = []

            # Agregar los datos a la página (tabla u otros elementos)
            for kardex in queryset:
                data = [
                    ['Nombre del paciente', kardex.paciente],
                    ['Diagnóstico', kardex.diagnosis],
                    ['Dieta', kardex.dieta],
                    ['Edad', kardex.edad],
                    ['Peso', kardex.peso],
                    ['Tratamiento', Paragraph(kardex.tratamiento, styles["Normal"])],
                    ['Plan', Paragraph(kardex.plan, styles["Normal"])],
                    ['Fecha de creación', kardex.fecha_kardex.strftime('%Y-%m-%d %H:%M:%S')],
                ]

                # Definir los estilos para la tabla
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
                table = Table(data)
                table.setStyle(table_style)
                page_content.append(table)

            # Agregar imagen de fondo (ajustar la ruta)
            background_image = 'web/static/img/bg/hoja-horizontal.jpg'  # Ruta correcta
            img = Image(background_image, width=doc.width, height=doc.height)

            # Ajustar la posición de la imagen
            img.wrapOn(doc, doc.leftMargin, doc.bottomMargin)
            img.drawOn(doc, 0, 0)

            # Agregar la imagen al contenido de la página
            page_content.append(img)

            # Agregar contenido de la página al documento
            content.extend(page_content)  # Usamos extend en lugar de append

        # Generar un nombre de archivo usando el nombre del paciente y la fecha de creación
        file_name = f"{slugify(kardex.paciente)}-{kardex.fecha_kardex.strftime('%d%m%y')}.pdf"
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'

        doc.build(content)

        pdf_buffer.seek(0)
        response.write(pdf_buffer.read())
        pdf_buffer.close()

        return response

    generate_pdf_action.short_description = "Generar PDF de Kardex"

admin.site.register(Kardex, KardexAdmin)
