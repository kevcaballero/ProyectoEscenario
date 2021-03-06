# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-26 18:11
from __future__ import unicode_literals

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
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Escenario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_escenario', models.CharField(max_length=200)),
                ('tipo_escenario', models.CharField(choices=[('O', 'Operativo'), ('A', 'Academico'), ('D', 'Deportivo'), ('C', 'Civico'), ('P', 'Pasillos'), ('R', 'Recreativo')], default='Default Value', max_length=1)),
                ('ubicacion', models.CharField(max_length=250)),
                ('estado', models.CharField(choices=[('O', 'Ocupado'), ('D', 'Disponible')], default='Disponible', max_length=1)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='escenarios')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_evento', models.CharField(max_length=200)),
                ('fecha_hora', models.DateTimeField(verbose_name='Fecha y hora del evento')),
                ('capacidad_evento', models.IntegerField(null=True, verbose_name='Capacidad del evento')),
                ('tipo_evento', models.CharField(choices=[('A', 'Academico'), ('D', 'Deportivo'), ('CRA', 'Cultural'), ('C', 'Civico'), ('R', 'Recreativo'), ('CAP', 'Capacitacion')], max_length=3)),
                ('objetivo', models.TextField(verbose_name='Objetivo')),
                ('publicar_medios', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=2, verbose_name='Publicar en medios?')),
                ('publicar_sito_web', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=2, verbose_name='Publicar en sitio web?')),
                ('publicar_social_media', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=2, verbose_name='Publicar en redes sociales?')),
                ('facebook_live', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=2, verbose_name='Transmitir en tiempo real (Facebook live)?')),
                ('musica_ambiente', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=2, verbose_name='Música de ambiente?')),
                ('laptop', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=2, verbose_name='Requiere laptop?')),
                ('microfonos', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=2, verbose_name='Requiere microfonos?')),
                ('internet', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=2)),
                ('escenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reserva.Escenario')),
            ],
        ),
        migrations.CreateModel(
            name='PresentacionEscenario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, verbose_name='Nombre de la presentacion')),
                ('presentacion', models.ImageField(default=' Default Value', upload_to='presentacion')),
                ('escenario', models.CharField(max_length=100, verbose_name='Tmp')),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='presentacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reserva.PresentacionEscenario'),
        ),
        migrations.AddField(
            model_name='evento',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comentario',
            name='evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reserva.Evento'),
        ),
    ]
