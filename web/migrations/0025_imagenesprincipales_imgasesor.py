# Generated by Django 4.2.5 on 2023-09-26 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0024_imagenesprincipales"),
    ]

    operations = [
        migrations.AddField(
            model_name="imagenesprincipales",
            name="imgasesor",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="web.asesor"
            ),
        ),
    ]
