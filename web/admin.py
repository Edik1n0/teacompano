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
from weasyprint import HTML

from .models import Kardex, Asesor, Formulario, Video, Pagina

class KardexAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'fecha_kardex', 'diagnosis', 'dieta', 'edad', 'peso', 'generate_pdf_link')
    actions = ['generate_pdf_action']

    def generate_pdf_link(self, obj):
        pdf_url = reverse('generate_pdf', args=[obj.id])
        return format_html('<a href="{}">Generar PDF</a>', pdf_url)
    
    generate_pdf_link.short_description = "PDF"

    def generate_pdf_action(self, request, queryset):
        pdf_buffer = BytesIO()
        html_content = self.get_html_content(queryset)
        
        # Use WeasyPrint to generate the PDF from HTML
        HTML(string=html_content).write_pdf(pdf_buffer)

        # Set response headers
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="kardex.pdf"'

        # Write PDF buffer data to response
        pdf_buffer.seek(0)
        response.write(pdf_buffer.read())
        pdf_buffer.close()

        return response

    generate_pdf_action.short_description = "Generar PDF de Kardex"

    def get_html_content(self, queryset):
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                /* Define your CSS styles here */
                body {
                    background-image: url('/web/static/img/bg/hoja-horizontal.jpg');
                    background-size: cover;
                    /* Other styles */
                }
                table {
                    /* Table styles */
                }
                /* Add more styles as needed */
            </style>
        </head>
        <body>
            <div class="container kardex">
                <h1 style="text-align: center;">Kardex</h1>
                <table style="width: 100%; border-collapse: collapse; margin-top: 20px;">
                    <!-- Table rows and data -->
                </table>
            </div>
        </body>
        </html>
        """

        return html_content

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
