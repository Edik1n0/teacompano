# Generated by Django 4.1.5 on 2023-07-26 15:40

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0003_alter_pagina_pagebanner_alter_pagina_pagebannermov"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pagina",
            name="pagemetadesc",
            field=ckeditor.fields.RichTextField(
                verbose_name="Meta descripción de la página"
            ),
        ),
    ]
