# Generated by Django 4.0.2 on 2022-02-04 01:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_de_creación', models.DateTimeField(auto_now_add=True)),
                ('fecha_de_publicación', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('titulo_curso', models.CharField(max_length=50)),
                ('descripcion_curso', models.TextField()),
                ('vigencia', models.DateTimeField(blank=True, null=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cursos', to=settings.AUTH_USER_MODEL)),
                ('persona_asignada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asignado', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Modulos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_de_creación', models.DateTimeField(auto_now_add=True)),
                ('fecha_de_publicación', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('archivos', models.FileField(max_length=20, null=True, upload_to='archivos_subidos')),
                ('cursos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modulos', to='cursos.curso')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_de_creación', models.DateTimeField(auto_now_add=True)),
                ('fecha_de_publicación', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('video', models.FileField(max_length=20, null=True, upload_to='videos')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField(null=True)),
                ('modulos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='cursos.modulos')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
