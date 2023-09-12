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
    
class S3ProductImage(S3Boto3Storage):
    location = 'teacompano-img'
    file_overwrite = False

class Galeria(models.Model):
    identificador = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='teacompano-img/')  # 'galeria/' es el directorio en S3 donde se guardarán las imágenes

    def __str__(self):
        return self.identificador

class Service(models.Model):
    # Elementos Visuales del servicio
    servicename = models.CharField(max_length=200, verbose_name="Nombre del servicio")
    serviceslogan = models.CharField(max_length=200, verbose_name="Slogan del servicio")
    # Elementos del header del servicio
    servicemetadesc = models.CharField(max_length=300, verbose_name="Meta descripción del servicio")
    servicemetatitle = models.CharField(max_length=200, verbose_name="Metatítulo(title) del servicio", default="Metatítulo por default")
    servicekeywords = RichTextField(verbose_name="Palabras clave del servicio")
    servicebanner = models.ImageField(upload_to='teacompano-img/', verbose_name="Imagen Banner del servicio", default='/servicios/static/img/default.jpg')
    servicebannermov = models.ImageField(upload_to='teacompano-img/', verbose_name="Imagen Banner del servicio en Móvil", default='/servicios/static/img/default-mov.jpg')
    # Elementos OG del servicio
    serviceogurl = models.CharField(max_length=200, verbose_name="Url OG del servicio")
    serviceogdesc = models.CharField(max_length=400, verbose_name="Descripción OG del servicio", default='Descripción del servicio')
    serviceogimg = models.CharField(max_length=200, verbose_name="Url OG Microformato del servicio")
    serviceogurlsec = models.CharField(max_length=200, verbose_name="Url OG Segura del servicio")
    serviceurl = models.CharField(max_length=200, verbose_name="Url servicio detalle")
    servicedescription = RichTextField(verbose_name="Descripción del servicio")
    serviceimg = models.ImageField(upload_to='teacompano-img/', verbose_name="Imagen principal del servicio")
    gallerya = models.ImageField(upload_to='teacompano-img/', verbose_name="Imagen secundaria del servicio", blank=True)
    galleryb = models.ImageField(upload_to='teacompano-img/', verbose_name="Imagen adicional del servicio", blank=True)
    galleryc = models.ImageField(upload_to='teacompano-img/', verbose_name="Imagen final del servicio", blank=True)
    # productimg = models.ImageField(upload_to='static/img/uploads/', verbose_name="Imagen principal del servicio")
    asesor = models.ForeignKey(Asesor, on_delete=models.SET_NULL, null=True)
    # productprice = models.IntegerField(verbose_name="Precio de venta", blank=True, null=True, editable=False)
    serviceupdated = models.DateTimeField(auto_now=True)

    #Snipets
    servicesnipeta = models.CharField(max_length=400, verbose_name="Primer snipet del servicio", blank=True, default="Snipet por default")
    servicesnipetb = models.CharField(max_length=400, verbose_name="Segundo snipet del servicio", blank=True, default="Snipet por default")
    servicesnipetc = models.CharField(max_length=400, verbose_name="Tercer snipet del servicio", blank=True, default="Snipet por default")
    servicesnipetd = models.CharField(max_length=400, verbose_name="Cuarto snipet del servicio", blank=True, default="Snipet por default")

    def __str__(self):
        return self.servicename + ' - creado por - ' + self.asesor.name

    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'pk': self.pk})

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
    pagebanner = models.ImageField(upload_to='teacompano-img/', verbose_name="Imagen Banner de la página", default='/servicios/static/img/default.jpg')
    pagebannermov = models.ImageField(upload_to='teacompano-img/', verbose_name="Imagen Banner de la página en Móvil", default='/servicios/static/img/default-mov.jpg')
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
    servicio = models.CharField(max_length=200, choices=SERVICE_CHOICES, verbose_name="servicio solicitado", blank=True)

    def __str__(self):
        return self.nombre
    
class Kardex(models.Model):
    paciente = models.CharField(max_length=200, verbose_name="Nombre del paciente", blank=True)
    diagnosis = models.CharField(max_length=200, verbose_name="Diagnóstico", blank=True)
    dieta = models.CharField(max_length=200, verbose_name="Dieta", blank=True)
    oxigeno = models.CharField(max_length=200, verbose_name="Oxigeno", blank=True)
    edad = models.CharField(max_length=200, verbose_name="Edad", blank=True)
    peso = models.CharField(max_length=200, verbose_name="Peso", blank=True)
    tratamiento = RichTextField(verbose_name="Tratamiento Farmacológico", blank=True)
    plan = RichTextField(verbose_name="Plan de cuidados de enfermería", blank=True)
    fecha_kardex = models.DateTimeField(default=timezone.now)

    def __str__(self):
        fecha_formateada = self.fecha_kardex.strftime('%Y-%m-%d %H:%M:%S')  # Formatea la fecha como quieras
        return f"{self.paciente} - {fecha_formateada}"