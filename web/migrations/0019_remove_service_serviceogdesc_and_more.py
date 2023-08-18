# Generated by Django 4.1.5 on 2023-08-18 14:41

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0018_service_servicemetatitle"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="service",
            name="serviceogdesc",
        ),
        migrations.AlterField(
            model_name="formulario",
            name="servicio",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Enfermería", "Enfermeria"),
                    ("Consulta Médica", "Consulta Médica"),
                    ("Consulta Psicología", "Consulta Psicología"),
                    ("Fisioterapia", "Terapia Física"),
                    ("Consulta Jurídica", "Consulta Jurídica"),
                ],
                max_length=200,
                verbose_name="servicio solicitado",
            ),
        ),
        migrations.AlterField(
            model_name="pagina",
            name="pagebanner",
            field=models.ImageField(
                default="/servicios/static/img/default.jpg",
                upload_to="teacompano-img/",
                verbose_name="Imagen Banner de la página",
            ),
        ),
        migrations.AlterField(
            model_name="pagina",
            name="pagebannermov",
            field=models.ImageField(
                default="/servicios/static/img/default-mov.jpg",
                upload_to="teacompano-img/",
                verbose_name="Imagen Banner de la página en Móvil",
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="gallerya",
            field=models.ImageField(
                blank=True,
                upload_to="teacompano-img/",
                verbose_name="Imagen secundaria del servicio",
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="galleryb",
            field=models.ImageField(
                blank=True,
                upload_to="teacompano-img/",
                verbose_name="Imagen adicional del servicio",
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="galleryc",
            field=models.ImageField(
                blank=True,
                upload_to="teacompano-img/",
                verbose_name="Imagen final del servicio",
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="servicebanner",
            field=models.ImageField(
                default="/servicios/static/img/default.jpg",
                upload_to="teacompano-img/",
                verbose_name="Imagen Banner del servicio",
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="servicebannermov",
            field=models.ImageField(
                default="/servicios/static/img/default-mov.jpg",
                upload_to="teacompano-img/",
                verbose_name="Imagen Banner del servicio en Móvil",
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="servicedescription",
            field=ckeditor.fields.RichTextField(
                verbose_name="Descripción del servicio"
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="serviceimg",
            field=models.ImageField(
                upload_to="teacompano-img/",
                verbose_name="Imagen principal del servicio",
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="servicekeywords",
            field=ckeditor.fields.RichTextField(
                verbose_name="Palabras clave del servicio"
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="servicemetadesc",
            field=models.CharField(
                max_length=300, verbose_name="Meta descripción del servicio"
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="servicemetatitle",
            field=models.CharField(
                default="Metatítulo por default",
                max_length=200,
                verbose_name="Metatítulo(title) del servicio",
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="servicename",
            field=models.CharField(max_length=200, verbose_name="Nombre del servicio"),
        ),
        migrations.AlterField(
            model_name="service",
            name="serviceogimg",
            field=models.CharField(
                max_length=200, verbose_name="Url OG Microformato del servicio"
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="serviceogurl",
            field=models.CharField(max_length=200, verbose_name="Url OG del servicio"),
        ),
        migrations.AlterField(
            model_name="service",
            name="serviceogurlsec",
            field=models.CharField(
                max_length=200, verbose_name="Url OG Segura del servicio"
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="serviceslogan",
            field=models.CharField(max_length=200, verbose_name="Slogan del servicio"),
        ),
        migrations.AlterField(
            model_name="service",
            name="serviceurl",
            field=models.CharField(max_length=200, verbose_name="Url servicio detalle"),
        ),
    ]