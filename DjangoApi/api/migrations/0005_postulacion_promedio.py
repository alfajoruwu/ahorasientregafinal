# Generated by Django 5.0.4 on 2024-06-09 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_modulo_unique_modulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='postulacion',
            name='promedio',
            field=models.FloatField(default=0.0),
        ),
    ]