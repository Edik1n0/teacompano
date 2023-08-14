# Generated by Django 4.1.5 on 2023-07-27 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0009_formulario"),
    ]

    operations = [
        migrations.AlterField(
            model_name="formulario",
            name="celular",
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name="formulario",
            name="descripcion",
            field=models.TextField(blank=True, verbose_name="Descripción del paciente"),
        ),
        migrations.AlterField(
            model_name="formulario",
            name="nombre",
            field=models.CharField(
                blank=True, max_length=200, verbose_name="Nombre del usuario"
            ),
        ),
    ]