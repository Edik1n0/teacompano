# Generated by Django 4.1.5 on 2023-08-17 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0017_remove_service_serviceogtitle"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="servicemetatitle",
            field=models.CharField(
                default="Metatítulo por default",
                max_length=200,
                verbose_name="Metatítulo(title) del Servicio",
            ),
        ),
    ]