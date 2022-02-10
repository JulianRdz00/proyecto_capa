# Generated by Django 4.0.2 on 2022-02-09 00:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cursos', '0002_alter_curso_persona_asignada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='persona_asignada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asignado', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='modulos',
            name='archivos',
            field=models.FileField(blank=True, max_length=20, null=True, upload_to='archivos_subidos'),
        ),
        migrations.AlterField(
            model_name='video',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(blank=True, max_length=20, null=True, upload_to='videos'),
        ),
    ]
