# Generated by Django 4.0.4 on 2022-06-11 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('golpe', '0002_golpe_tipo_erro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='golpe',
            name='tipo_erro',
        ),
    ]
