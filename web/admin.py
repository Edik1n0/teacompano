from django.contrib import admin
from reportlab.platypus import SimpleDocTemplate, PageTemplate, Frame, Image
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
from django.utils.text import slugify
from django.http import HttpResponse
from django.urls import reverse
from django.utils.html import format_html

from .models import Kardex, Asesor, Formulario, Video, Pagina

class KardexAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'fecha_kardex', 'diagnosis', 'dieta', 'edad', 'peso', 'generate_pdf_link')
    actions = ['generate_pdf_action']

    def generate_pdf_link(self, obj):
        pdf_url = reverse('generate_pdf', args=[obj.id])
        return format_html('<a href="{}">Generar PDF</a>', pdf_url)
    
    generate_pdf_link.short_description = "PDF"

    def generate_pdf_action(self, request, queryset):
        styles = getSampleStyleSheet()
        pdf_buffer = BytesIO()

        # Crear un documento PDF
        doc = SimpleDocTemplate(pdf_buffer, pagesize=landscape(letter))

        content = []

        for kardex in queryset:
            # Crear una lista para el contenido de la página
            page_content = []

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

            # Debug: Verificar si la imagen se carga correctamente
            print("Ruta de la imagen:", background_image)

            # Crear un PageTemplate con la imagen de fondo
            img = Image(background_image, width=doc.width, height=doc.height)
            img_frame = Frame(0, 0, doc.width, doc.height)
            img_frame.addFromList([img], doc)
            template = PageTemplate(id='background', frames=[img_frame])
            doc.addPageTemplates([template])

            # Debug: Verificar si el PageTemplate se crea correctamente
            print("PageTemplate creado con la imagen de fondo:", template)

            # Agregar contenido de la página al documento
            content.extend(page_content)

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

admin.site.register(Asesor)
admin.site.register(Pagina)
admin.site.register(Video)

class FormularioAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_solicitud', 'servicio')

    def get_timezone(self, obj):
        return obj.fecha_solicitud.timezone  # Retorna el valor de timezone de la fecha_solicitud

    #get_timezone.short_description = 'Timezone'  # Nombre descriptivo para el campo en el admin

admin.site.register(Formulario, FormularioAdmin)
