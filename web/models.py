from django.db import models
from ckeditor.fields import RichTextField
from storages.backends.s3boto3 import S3Boto3Storage
from django.urls import reverse
from django.utils import timezone

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
    pagemetadesc = models.CharField(max_length=200, verbose_name="Meta descripción de la página")
    pagekeywords = RichTextField(verbose_name="Palabras clave de la página")
    pagebanner = models.ImageField(upload_to='teacompano-img/', verbose_name="Imagen Banner de la página", default='/productos/static/img/default.jpg')
    pagebannermov = models.ImageField(upload_to='teacompano-img/', verbose_name="Imagen Banner de la página en Móvil", default='/productos/static/img/default-mov.jpg')
    pageogdesc = models.CharField(max_length=200, verbose_name="Descripción OG de la página")
    pageogtitle = models.CharField(max_length=200, verbose_name="Título OG de la página")
    pageogurl = models.CharField(max_length=200, verbose_name="Url OG de la página")
    pageogimg = models.CharField(max_length=200, verbose_name="Url OG Microformato de la página")
    pageogurlsec = models.CharField(max_length=200, verbose_name="Url OG Segura de la página")

    def __str__(self):
        return self.pagename
    

