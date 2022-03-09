# Generated by Django 4.0.2 on 2022-02-17 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingles', models.CharField(blank=True, choices=[('Basico', 'Basico'), ('Intermedio', 'Intermedio'), ('Avanzado', 'Avanzado')], default='Nulo', max_length=12, null=True)),
                ('formacion_academica', models.TextField(blank=True, max_length=500, null=True)),
                ('profesion', models.TextField(blank=True, max_length=100, null=True)),
                ('fotos', models.ImageField(blank=True, null=True, upload_to='fotos')),
                ('webPage', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=100, null=True)),
                ('youtube', models.CharField(blank=True, max_length=100, null=True)),
                ('nacionalidad', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('genero', models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')], default='Nulo', max_length=12, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
