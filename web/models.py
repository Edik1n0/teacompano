from django.db import models
from ckeditor.fields import RichTextField
from storages.backends.s3boto3 import S3Boto3Storage
from django.urls import reverse
from django.utils import timezone
import pytz

# Create your models here.
class Asesor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Video(models.Model):
    videoname = models.CharField(max_length=200, verbose_name="Nombre del video")
    videourl = models.CharField(max_length=200, verbose_name="URL del video")

    def __str__(self):
        return self.videoname
    
class Pagina(models.Model):
    pagename = models.CharField(max_length=200, verbose_name="Nombre de la página")
    pagemetatitle = models.CharField(max_length=200, verbose_name="Metatítulo(title) de la página")
    pagetitle = models.CharField(max_length=200, verbose_name="Título(h1) de la página")
    pageslogan = models.CharField(max_length=200, verbose_name="Slogan(h2) de la página")
    pagemetadesc = RichTextField(verbose_name="Meta descripción de la página")
    pagekeywords = RichTextField(verbose_name="Palabras clave de la página")
    pagebanner = models.ImageField(upload_to='teacompano-img/', verbose_name="Imagen Banner de la página", default='/productos/static/img/default.jpg')
    pagebannermov = models.ImageField(upload_to='teacompano-img/', verbose_name="Imagen Banner de la página en Móvil", default='/productos/static/img/default-mov.jpg')
    pageogdesc = models.CharField(max_length=400, verbose_name="Descripción OG de la página", default='Descripción del sitio web')
    pageogurl = models.CharField(max_length=200, verbose_name="Url OG de la página")
    pageogimg = models.CharField(max_length=200, verbose_name="Url OG Microformato de la página")
    pageogurlsec = models.CharField(max_length=200, verbose_name="Url OG Segura de la página")

    def __str__(self):
        return self.pagename
    
class Formulario(models.Model):
    SERVICE_CHOICES = (
        ('Enfermería', 'Enfermeria'),
        ('Consulta Médica', 'Consulta Médica'),
        ('Consulta Psicología', 'Consulta Psicología'),
        ('Fisioterapia', 'Terapia Física'),
        ('Consulta Jurídica', 'Consulta Jurídica'),
    )

    nombre = models.CharField(max_length=200, verbose_name="Nombre del usuario", blank=True)
    correo = models.EmailField(verbose_name="Email del usuario")
    celular = models.CharField(max_length=15, blank=True)
    descripcion = models.TextField(verbose_name="Descripción del paciente", blank=True)
    fecha_solicitud = models.DateTimeField(default=timezone.now)
    servicio = models.CharField(max_length=200, choices=SERVICE_CHOICES, verbose_name="Servicio solicitado", blank=True)

    def __str__(self):
        return self.nombre
    
class Kardex(models.Model):
    paciente = models.CharField(max_length=200, verbose_name="Nombre del paciente", blank=True)
    diagnosis = models.CharField(max_length=200, verbose_name="Diagnóstico", blank=True)
    dieta = models.CharField(max_length=200, verbose_name="Dieta", blank=True)
    edad = models.CharField(max_length=200, verbose_name="Edad", blank=True)
    peso = models.CharField(max_length=200, verbose_name="Peso", blank=True)
    tratamiento = RichTextField(verbose_name="Tratamiento Farmacológico", blank=True)
    plan = RichTextField(verbose_name="Plan de cuidados de enfermería", blank=True)
    fecha_kardex = models.DateTimeField(default=timezone.now)

    def __str__(self):
        fecha_formateada = self.fecha_kardex.strftime('%Y-%m-%d %H:%M:%S')  # Formatea la fecha como quieras
        return f"{self.paciente} - {fecha_formateada}"