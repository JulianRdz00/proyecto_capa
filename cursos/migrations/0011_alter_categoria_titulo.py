# Generated by Django 4.0.2 on 2022-02-25 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0010_alter_categoria_fecha_de_creación_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='titulo',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
