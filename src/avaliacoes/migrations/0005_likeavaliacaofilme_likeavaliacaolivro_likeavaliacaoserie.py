# Generated by Django 3.1.7 on 2021-05-26 12:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('avaliacoes', '0004_auto_20210525_0025'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeAvaliacaoSerie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avaliacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avaliacoes.avaliacaoserie')),
                ('user_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user_id')),
            ],
            options={
                'verbose_name': 'Like',
                'verbose_name_plural': 'Likes',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LikeAvaliacaoLivro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avaliacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avaliacoes.avaliacaolivro')),
                ('user_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user_id')),
            ],
            options={
                'verbose_name': 'Like',
                'verbose_name_plural': 'Likes',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LikeAvaliacaoFilme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avaliacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avaliacoes.avaliacaofilme')),
                ('user_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user_id')),
            ],
            options={
                'verbose_name': 'Like',
                'verbose_name_plural': 'Likes',
                'abstract': False,
            },
        ),
    ]