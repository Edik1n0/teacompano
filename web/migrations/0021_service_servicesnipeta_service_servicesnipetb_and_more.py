# Generated by Django 4.1.5 on 2023-08-18 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0020_service_serviceogdesc"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="servicesnipeta",
            field=models.CharField(
                blank=True,
                default="Snipet por default",
                max_length=400,
                verbose_name="Primer snipet del servicio",
            ),
        ),
        migrations.AddField(
            model_name="service",
            name="servicesnipetb",
            field=models.CharField(
                blank=True,
                default="Snipet por default",
                max_length=400,
                verbose_name="Segundo snipet del servicio",
            ),
        ),
        migrations.AddField(
            model_name="service",
            name="servicesnipetc",
            field=models.CharField(
                blank=True,
                default="Snipet por default",
                max_length=400,
                verbose_name="Tercer snipet del servicio",
            ),
        ),
        migrations.AddField(
            model_name="service",
            name="servicesnipetd",
            field=models.CharField(
                blank=True,
                default="Snipet por default",
                max_length=400,
                verbose_name="Cuarto snipet del servicio",
            ),
        ),
    ]