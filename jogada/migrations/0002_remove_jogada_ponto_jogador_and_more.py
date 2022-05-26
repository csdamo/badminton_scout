# Generated by Django 4.0.4 on 2022-05-26 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jogador', '0002_jogador_foto'),
        ('jogada', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jogada',
            name='ponto_jogador',
        ),
        migrations.RemoveField(
            model_name='jogada',
            name='ponto_jogador_adversario',
        ),
        migrations.RemoveField(
            model_name='jogada',
            name='status',
        ),
        migrations.AlterField(
            model_name='jogada',
            name='jogador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jogador.jogador'),
        ),
    ]
