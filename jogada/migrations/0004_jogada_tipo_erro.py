# Generated by Django 4.0.4 on 2022-06-11 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tipoerro', '0001_initial'),
        ('jogada', '0003_jogada_acerto'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogada',
            name='tipo_erro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tipoerro.tipoerro'),
        ),
    ]
