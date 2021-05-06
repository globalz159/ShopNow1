# Generated by Django 3.1.7 on 2021-05-06 01:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('publicacoes', '0001_initial'),
        ('comentarios', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='user_id'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='comentario_pai',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='comentarios.comentario'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='publicacao',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='publicacoes.publicacao'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
