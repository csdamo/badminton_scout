# Generated by Django 4.0.4 on 2022-04-28 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partida', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partida',
            name='nome',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
